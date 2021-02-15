from django.urls import path,include
from .views import (
        SubscriptionViewSet,
        SubscriptionNotificationsViewSet
    )



from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'subscription', SubscriptionViewSet)
router.register(r'subscription-notifications', SubscriptionNotificationsViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('utils', include('utils.urls'))

]
