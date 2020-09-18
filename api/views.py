from rest_framework.response import Response
from rest_framework.views import APIView


class Register(APIView):
    def post(self, request, format=None):
        return Response("ok", status=200)
