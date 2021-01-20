from rest_framework import generics, status, views, permissions
from .serializers import UploadSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import xlsxwriter

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
from io import BytesIO
import pdftotext
from .doc2pdf import doc2pdf
from .imgpdf import custom_img2pdf,custom_img_png_2pdf
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
        zip_dir = unique_filename+'.zip'
        with zipfile.ZipFile(zip_dir, 'w') as myzip:         
            for index,page in enumerate(file_path_image):
                page[0].save(os.path.join(save_dir, file_name_image[index]), 'JPEG')
                myzip.write(os.path.join(save_dir, file_name_image[index]))


        response = FileResponse(open(zip_dir, 'rb'),filename=data._name+'.zip')
        os.remove(tmp_file)
        shutil.rmtree(save_dir)
        os.remove(zip_dir)
        return response


class FileUploadPdfToExcelView(views.APIView):
    serializer_class = UploadSerializer
    def post(self, request,format=None):
        data = request.data['file']
        if data.content_type != 'application/pdf':
            return Response(status=400)
        
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        pdf = []

        with open('data-1.pdf', 'rb') as pdf_file:
            pdf = pdftotext.PDF(pdf_file)

        count = 1
        for item in pdf:
            for i in item.split("\n"):
                print(i)
                worksheet.set_column(0, 0, 550)
                print(len(i))
                worksheet.write('A'+str(count),str(i))
                count = count +1

        # for page in range(pdf_reader.getNumPages()):
        #     print(pdf_reader.getPage(page).extractText())
        #     text = pdf_reader.getPage(page).extractText().split("\n")
        #     for i in range(len(text)):
        #         # Printing the line
        #     # Lines are seprated using "\n"
        #         print(text[i],"\n",'-----------')
        #     # print(text)
        #     break
        #     # worksheet.write('A'+str(page),)
       
        workbook.close()
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename="'+'test'+".xlsx"
        response.write(output.getvalue())
        return response

class FileUploadImageToPDFView(views.APIView):
    serializer_class = UploadSerializer
    def post(self, request,format=None):
        data = request.data['file']
        print(data.__dict__)
        if data.content_type == 'image/jpeg' or data.content_type == 'image/png':
            unique_filename = str(uuid.uuid4())
            file_path = 'image/'+unique_filename+'.'+data.content_type.split('/')[1]
            path = default_storage.save(file_path, ContentFile(data.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            pdf_path ='pdf/'+unique_filename+'.pdf'
            if data.content_type == 'image/png':
                custom_img_png_2pdf(file_path,pdf_path)
            else:
                custom_img2pdf(file_path,pdf_path)
            response = FileResponse(open(pdf_path, 'rb'),filename=data._name+'.pdf')
            os.remove(tmp_file)
            os.remove(pdf_path)
            return response
        else:
            return Response(status=400)
        

class FileUploadDocxToPDFView(views.APIView):
    serializer_class = UploadSerializer
    def post(self, request,format=None):
        data = request.data['file']
        print(data.__dict__)
        if data.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            unique_filename = str(uuid.uuid4())
            file_path = 'docx/'+unique_filename+'.docx'
            path = default_storage.save(file_path, ContentFile(data.read()))
            tmp_file = os.path.join(settings.MEDIA_ROOT, path)
            pdf_path ='pdf/'+unique_filename+'.pdf'
            print(tmp_file,'--------',pdf_path)
            l = doc2pdf(tmp_file,pdf_path)
            print('ancav',l)
            response = FileResponse(open(pdf_path, 'rb'),filename=data._name+'.docx')
            os.remove(tmp_file)
            os.remove(pdf_path)
            return response
        else:
            return Response(status=400)



# custom_img2pdf('update0.3 Project Requirements documentation.jpg','test.pdf')

# doc2pdf('update0.3 Project Requirements documentation.docx')

# custom_img2pdf("image/b7fcf191-8319-4ba3-bcff-fa46452fec22.png",  "pdf/b7fcf191-8319-4ba3-bcff-fa46452fec22.pdf")
# doc2pdf('docx/c826c8f9-b9b5-4dbf-8858-0430c6560b08.docx','pdf/c826c8f9-b9b5-4dbf-8858-0430c6560b08.pdf')
