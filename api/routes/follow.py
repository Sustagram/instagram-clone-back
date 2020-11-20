import json

from rest_framework.response import Response
from rest_framework.views import APIView

from ..errors import VALIDATION_ERROR
from ..forms import FollowForm
from ..models import Subscribe
from ..serializers import SubscribeSerializer
from ..utils import make_response_payload, require_token


class Follow(APIView):
    @require_token
    def post(self, request):
        if request.META["CONTENT_TYPE"] != "application/json":
            return Response(make_response_payload(is_success=False), status=415)

        body = json.loads(request.body)
        form = FollowForm(data=body)

        if not form.is_valid():
            return Response(make_response_payload(is_success=False, message=VALIDATION_ERROR), status=400)

        follow = Subscribe.objects.create(
            user_id_id=request.user["user_id"],
            following_id_id=body["followingId"]
        )

        return Response(make_response_payload(SubscribeSerializer(follow).data), status=200)

    @require_token
    def delete(self, request):
        if request.META["CONTENT_TYPE"] != "application/json":
            return Response(make_response_payload(is_success=False), status=415)

        body = json.loads(request.body)
        form = FollowForm(data=body)

        if not form.is_valid():
            return Response(make_response_payload(is_success=False, message=VALIDATION_ERROR), status=400)

        follow = Subscribe.objects.filter(
            user_id_id=request.user["user_id"],
            following_id_id=body["followingId"]
        ).delete()

        return Response(make_response_payload(), status=200)
