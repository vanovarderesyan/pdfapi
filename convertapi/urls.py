from django.urls import path
from .views import FileUploadView



urlpatterns = [

    path('pdf-to-word/', FileUploadView.as_view())
]
