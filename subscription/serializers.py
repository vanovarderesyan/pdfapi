from rest_framework import serializers
from .models import Subscription,SubscriptionNotifications


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionNotifications
        fields = '__all__'