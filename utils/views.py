from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContactSerializer
from .models import Contact
# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


