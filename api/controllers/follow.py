from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Subscribe, User
from ..serializers import SubscribeSerializer, UserSerializer
from ..utils import make_response_payload, require_token


class FollowNotParams(APIView):
    @require_token
    def get(self, request):
        user_id = request.user['user_id']
        my_follow = Subscribe.objects.filter(user_id=user_id).all()

        result = []
        for value in my_follow:
            data = SubscribeSerializer(value).data
            user_data = User.objects.filter(user_id=data['user_id']).all()[0]
            data['following_username'] = UserSerializer(user_data).data['username']
            data['following_realname'] = UserSerializer(user_data).data['realname']
            result.append(data)

        return Response(make_response_payload(result), status=200)


class Follow(APIView):
    @require_token
    def post(self, request, follow_id):
        follow = Subscribe.objects.create(
            user_id_id=request.user["user_id"],
            following_id_id=follow_id
        )

        return Response(make_response_payload(SubscribeSerializer(follow).data), status=200)

    @require_token
    def delete(self, request, follow_id):
        current = Subscribe.objects.get(user_id_id=request.user["user_id"], following_id_id=follow_id)

        Subscribe.objects.filter(
            user_id_id=request.user["user_id"],
            following_id_id=follow_id
        ).delete()

        return Response(make_response_payload(SubscribeSerializer(current).data), status=200)
