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
import zipfile
from django.http import FileResponse
from io import StringIO
from PyPDF2 import PdfFileReader
import shutil

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


class FileUploadPdfToImageView(views.APIView):
    serializer_class = UploadSerializer

    def post(self, request,format=None):
        data = request.data['file']
        if data.content_type != 'application/pdf':
            return Response(status=400)
        
        unique_filename = str(uuid.uuid4())
        file_path = 'pdf/'+unique_filename+'.pdf'
        path = default_storage.save(file_path, ContentFile(data.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        filename = tmp_file
        images = convert_from_path(file_path,500)
        count_page_pdf = 0
        file_path_image= []
        file_name_image= []

        with open(file_path, "rb") as pdf_file:
            pdf_reader = PdfFileReader(pdf_file)
            count_page_pdf = pdf_reader.numPages
        
        print(count_page_pdf,'sssssssssss')
        with tempfile.TemporaryDirectory() as path:
            for item in range(count_page_pdf):
                print(item,'--------')
                file_path_image.append( convert_from_path(filename, output_folder=path, last_page=item+2, first_page = item+1))

                file_name_image.append(os.path.splitext(os.path.basename(filename))[0]+str(item) + '.jpg')     

        save_dir = './image/'+ unique_filename
        os.mkdir(save_dir)
        print(file_path_image,'-----------------')
        zip_dir = unique_filename+'.zip'
        with zipfile.ZipFile(zip_dir, 'w') as myzip:         
            for index,page in enumerate(file_path_image):
                print(page,'page')
                page[0].save(os.path.join(save_dir, file_name_image[index]), 'JPEG')
            
                myzip.write(os.path.join(save_dir, file_name_image[index]))
                print(file_name_image[index],'*********',os.path.join(save_dir, file_name_image[index]))


        response = FileResponse(open(zip_dir, 'rb'),filename=data._name+'.zip')
        os.remove(tmp_file)
        shutil.rmtree(save_dir)
        os.remove(zip_dir)
        return response
