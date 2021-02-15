from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SubscriptionSerializer,SubscriptionNotificationsSerializer
from .models import Subscription,SubscriptionNotifications
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
