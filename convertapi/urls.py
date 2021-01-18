from django.urls import path
from .views import FileUploadView,FileUploadPdfToImageView



urlpatterns = [

    path('pdf-to-word/', FileUploadView.as_view()),
    path('pdf-to-image/', FileUploadPdfToImageView.as_view()),

    
]
