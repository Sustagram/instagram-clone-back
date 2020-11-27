import json

from rest_framework.response import Response
from rest_framework.views import APIView

from ..errors import VALIDATION_ERROR
from ..forms import PostForm
from ..models import Post, Subscribe, User
from ..serializers import UserSerializer, PostSerializer, SubscribeSerializer
from ..utils import make_response_payload, require_token


class MyPostAPI(APIView):
    @require_token
    def get(self, request):
        mypost = Post.objects.filter(user_id=UserSerializer(request.user).data['user_id']).all().order_by('-created_at')
        result = []
        for post in mypost:
            data = PostSerializer(post).data
            user_data = User.objects.filter(user_id=data['user_id']).all()[0]
            data['username'] = UserSerializer(user_data).data['username']
            result.append(data)

        return Response(make_response_payload(result), status=200)


class PostAPI(APIView):
    @require_token
    def get(self, request):
        followers = Subscribe.objects.filter(user_id=UserSerializer(request.user).data['user_id']).all()

        result = []
        for f in followers:
            followerid = SubscribeSerializer(f).data['following_id']
            posts = Post.objects.filter(user_id=followerid).all().order_by('-created_at')
            for p in posts:
                data = PostSerializer(p).data
                user_data = User.objects.filter(user_id=data['user_id']).all()[0]
                data['username'] = UserSerializer(user_data).data['username']
                result.append(data)

        return Response(make_response_payload(result), status=200)


class PostUploadAPI(APIView):
    @require_token
    def post(self, request):
        if request.META["CONTENT_TYPE"] != "application/json":
            return Response(make_response_payload(is_success=False), status=415)

        body = json.loads(request.body)
        form = PostForm(data=body)

        if not form.is_valid():
            return Response(make_response_payload(is_success=False, message=VALIDATION_ERROR), status=400)

        post = Post.objects.create(
            text=body["text"],
            media=body["media"],
            user_id_id=body["userId"]
        )

        return Response(make_response_payload(PostSerializer(post).data), status=200)
