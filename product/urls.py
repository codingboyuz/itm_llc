from django.urls import path
from .views import ProductsPage

urlpatterns = [
    path('products/', ProductsPage.as_view(), name='products'),
]
