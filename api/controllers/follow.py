from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Subscribe
from ..serializers import SubscribeSerializer
from ..utils import make_response_payload, require_token


class FollowNotParams(APIView):
    @require_token
    def get(self, request):
        if request.META["CONTENT_TYPE"] != "application/json":
            return Response(make_response_payload(is_success=False), status=415)

        user_id = request.user['user_id']
        my_follow = Subscribe.objects.filter(user_id=user_id).all()

        result = []
        for value in my_follow:
            result.append(SubscribeSerializer(value).data)

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
