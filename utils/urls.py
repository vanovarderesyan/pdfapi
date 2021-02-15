from django.urls import path,include
from .views import (
        ContactViewSet
    )



from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'contact', ContactViewSet)


urlpatterns = [
    path('', include(router.urls))
]
