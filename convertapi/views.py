from rest_framework import generics, status, views, permissions
from .serializers import UploadSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

import jwt
from django.conf import settings
from drf_yasg import openapi
from django.http import HttpResponsePermanentRedirect
import os
from pdf2docx import Converter
from pdf2image import convert_from_path, convert_from_bytes
import os
import tempfile
from django.http import HttpResponse
from docx import Document
from rest_framework.parsers import FileUploadParser
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from django.core.files.storage import default_storage
import time
import csv
from django.core.files.base import ContentFile
import uuid

from django.http import FileResponse

class FileUploadView(views.APIView):
    serializer_class = UploadSerializer

    def post(self, request,format=None):
        data = request.data['file']
        print(data.__dict__)
        if data.content_type != 'application/pdf':
            return Response(status=400)
            
        unique_filename = str(uuid.uuid4())
        docs_file_name_path = 'docx/'+unique_filename+ '.docx'
        file_path = 'pdf/'+unique_filename+'.pdf'
        path = default_storage.save(file_path, ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        cv = Converter(tmp_file)
        cv.convert(docs_file_name_path, start=0, end=None)
        cv.close()
        response = FileResponse(open(docs_file_name_path, 'rb'),filename=data._name+'.docx')
        os.remove(docs_file_name_path)
        os.remove(tmp_file)
        return response
