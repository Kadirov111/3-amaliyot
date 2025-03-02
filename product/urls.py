from django.urls import path
from .views import ProductAPIView

urlpatterns = [
    path('api/product/', ProductAPIView.as_view(), name='product-list'),
]
