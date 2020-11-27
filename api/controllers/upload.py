import os
from datetime import datetime

import boto3
from rest_framework.response import Response
from rest_framework.views import APIView

from ..errors import VALIDATION_ERROR
from ..forms import UploadForm
from ..utils import make_response_payload, require_token

REGION_NAME = "ap-northeast-2"
BUCKET_NAME = "sustagram"

session = boto3.Session(
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name=REGION_NAME
)
s3 = session.resource('s3')


class UploadAPI(APIView):
    @require_token
    def post(self, request):
        form = UploadForm(request.POST, request.FILES)

        if not form.is_valid():
            return Response(make_response_payload(is_success=False, message=VALIDATION_ERROR), status=400)

        file = request.FILES['file']
        dt_string = datetime.now().strftime("%Y%m%d%M%M%S")
        file_name = f'{dt_string}-{file.name}'

        s3.Object(BUCKET_NAME, file_name).put(Body=file)

        file_url = f"https://s3.ap-northeast-2.amazonaws.com/{BUCKET_NAME}/{file_name}"

        return Response(make_response_payload(file_url), status=201)
