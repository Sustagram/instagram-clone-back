import datetime
import json

import uuid
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class Register(APIView):
    def post(self, request, format=None):
        if request.META["CONTENT_TYPE"] != "application/json":
            return
        body = json.loads(request.body)
        user = User(
            user_id=uuid.uuid4(),
            email=body["email"],
            realname=body["realname"],
            username=body["username"],
            password=body["password"],
            last_login=datetime.datetime.now()
        )
        user.save()
        return Response(status=201)
