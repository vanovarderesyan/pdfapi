from django.urls import path,include
from .views import (
    FileUploadView,
    FileUploadPdfToImageView,
    FileUploadPdfToExcelView
    ,FileUploadImageToPDFView,
    FileUploadDocxToPDFView,
    FileUploadXLSToPDFView
    )




urlpatterns = [

    path('pdf-to-word/', FileUploadView.as_view()),
    path('pdf-to-image/', FileUploadPdfToImageView.as_view()),
    path('pdf-to-excel/', FileUploadPdfToExcelView.as_view()),
    path('image-to-pdf/', FileUploadImageToPDFView.as_view()),
    path('docx-to-pdf/', FileUploadDocxToPDFView.as_view()),
    path('xls-to-pdf/', FileUploadXLSToPDFView.as_view()),


]
