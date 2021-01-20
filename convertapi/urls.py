from django.urls import path
from .views import (
    FileUploadView,
    FileUploadPdfToImageView,
    FileUploadPdfToExcelView
    ,FileUploadImageToPDFView,
    FileUploadDocxToPDFView
    )




urlpatterns = [

    path('pdf-to-word/', FileUploadView.as_view()),
    path('pdf-to-image/', FileUploadPdfToImageView.as_view()),
    path('pdf-to-excel/', FileUploadPdfToExcelView.as_view()),
    path('image-to-pdf/', FileUploadImageToPDFView.as_view()),
    path('docx-to-pdf/', FileUploadDocxToPDFView.as_view()),




    
]
