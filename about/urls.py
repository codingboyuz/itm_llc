from django.urls import path
from .views import AboutView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
]