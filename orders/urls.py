from django.urls import path, include
from rest_framework import routers

from .views import *
app_name = 'orders'

router = routers.DefaultRouter()
router.register('safe_order_and_send_email', OrderSafeAndSendEmailViewSet, basename='safe_order_and_send_email')

urlpatterns = [
    path('', include(router.urls))
]
