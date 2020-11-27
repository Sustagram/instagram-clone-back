from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Like
from ..serializers import LikeSerializer
from ..utils import make_response_payload, require_token


class LikeAPI(APIView):
    @require_token
    def post(self, request, post_id):
        user_id = request.user["user_id"]

        like = Like.objects.create(
            user_id_id=user_id,
            post_id_id=post_id
        )

        return Response(make_response_payload(LikeSerializer(like).data), status=200)

    @require_token
    def delete(self, request, post_id):
        user_id = request.user["user_id"]
        current = Like.objects.get(user_id_id=user_id, post_id_id=post_id)

        Like.objects.filter(
            user_id_id=user_id,
            post_id_id=post_id
        ).delete()

        return Response(make_response_payload(LikeSerializer(current).data), status=200)

    @require_token
    def get(self, request, post_id):
        user_id = request.user["user_id"]

        is_exist = Like.objects.filter(user_id_id=user_id, post_id_id=post_id).exists()

        return Response(make_response_payload(is_exist), status=200)


class LikeDataAPI(APIView):
    @require_token
    def get(self, request, post_id):
        data = Like.objects.filter(post_id_id=post_id).all()
        return Response(make_response_payload(LikeSerializer(data, many=True).data), status=200)
