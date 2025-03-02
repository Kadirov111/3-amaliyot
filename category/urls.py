from django.urls import path
from .views import CategoryAPIView

urlpatterns = [
    path('api/category/', CategoryAPIView.as_view(), name='category-list'),
]
