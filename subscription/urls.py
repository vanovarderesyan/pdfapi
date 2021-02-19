from django.urls import path,include
from .views import (
        SubscriptionViewSet,
        SubscriptionNotificationsViewSet,
        FAQViewSet
    )



from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'subscription', SubscriptionViewSet)
router.register(r'subscription-notifications', SubscriptionNotificationsViewSet)
router.register(r'faq', FAQViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('utils', include('utils.urls'))

]
