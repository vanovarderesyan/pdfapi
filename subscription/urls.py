from django.urls import path,include
from .views import (
        SubscriptionViewSet,
        SubscriptionNotificationsSerializer
    )



from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'subscription', SubscriptionViewSet)
router.register(r'subscription-notifications', SubscriptionViewSet)



urlpatterns = [
    path('', include(router.urls))
]
