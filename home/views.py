from django.views import View
from django.shortcuts import render
from .models import HomeModel
import logging

logger = logging.getLogger(__name__)

class HomePage(View):
    def get(self, request):
        try:
            data = HomeModel.objects.last()
            if data:
                return render(request, "home.html", {"data": data})
            # Ma'lumot yo‘q
            return render(request, "404.html", {"message": "Ma'lumot topilmadi!"})
        except Exception as e:
            logger.error(f"Home sahifasida xatolik: {str(e)}")
            return render(request, "error.html", {"message": "Noma'lum xatolik yuz berdi."})