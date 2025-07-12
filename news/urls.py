

from django.urls import path 
from .views import NewsView,NewsDetailView


urlpatterns = [
    path('',NewsView.as_view(),name='news'),
    path('<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
]