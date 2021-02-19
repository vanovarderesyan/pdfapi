from rest_framework import serializers
from .models import Subscription,SubscriptionNotifications,SubscriptionText,FAQ
class SubscriptionTextSerializerLoc(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionText
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    subscription_text = SubscriptionTextSerializerLoc(many=True,read_only=True)
        
    class Meta:
        depth=1
        model = Subscription
        fields = '__all__'


class SubscriptionNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionNotifications
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'