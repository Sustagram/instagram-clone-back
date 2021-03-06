import os

import jwt
from rest_framework.response import Response

from .errors import TOKEN_ERROR, USER_NOT_FOUND
from .models import User
from .serializers import UserSerializer


def make_response_payload(data=None, message=None, is_success=True):
    return {
        "success": is_success,
        "message": message,
        "data": data
    }


def require_token(func):
    def wrapper(self, request, *args, **kwargs):
        if not("HTTP_AUTHORIZATION" in request.META):
            return Response(make_response_payload(message=TOKEN_ERROR, is_success=True), status=401)

        token = str(request.META["HTTP_AUTHORIZATION"]).replace("Bearer ", "")
        try:
            decoded = jwt.decode(token, os.environ.get("SECRET_KEY"))
            user = User.objects.filter(user_id=decoded["uuid"])
            result = UserSerializer(user, many=True).data

            if len(result) <= 0:
                return Response(make_response_payload(message=USER_NOT_FOUND, is_success=True), status=404)

            request.user = result[0]

            return func(self, request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return Response(make_response_payload(message=TOKEN_ERROR, is_success=True), status=401)
        except jwt.InvalidSignatureError:
            return Response(make_response_payload(message=TOKEN_ERROR, is_success=True), status=401)
        except jwt.DecodeError:
            return Response(make_response_payload(message=TOKEN_ERROR, is_success=True), status=401)

    return wrapper
