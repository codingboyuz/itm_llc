from django.urls import path
from .views import ProductsView, ProductsDetailView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='product_detail'),
]
