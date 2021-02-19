from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SubscriptionSerializer,SubscriptionNotificationsSerializer,FAQSerializer
from .models import Subscription,SubscriptionNotifications,FAQ
# Create your views here.
class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionNotificationsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = SubscriptionNotifications.objects.all()
    serializer_class = SubscriptionNotificationsSerializer



class FAQViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer