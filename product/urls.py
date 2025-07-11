from django.urls import path
from .views import ProductsView, ProductsDetailView

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='product_detail'),
]
