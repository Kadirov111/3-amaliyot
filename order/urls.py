from django.urls import path
from .views import OrderAPIView

urlpatterns = [
    path('api/order/', OrderAPIView.as_view(), name='order-list'),
]
