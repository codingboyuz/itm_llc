from django.views import View
from django.shortcuts import render
from .models import ProductModel
import logging

logger = logging.getLogger(__name__)

class ProductsPage(View):
    def get(self, request):
        try:
            data = ProductModel.objects.all()

            print(f"==data=================={data}")

            if data:
                print(f"===================={data}")

                return render(request, "prducts.html", {"data": data})
            # Ma'lumot yo‘q
            return render(request, "404.html", {"message": "Ma'lumot topilmadi!"})
        except Exception as e:
            logger.error(f"Home sahifasida xatolik: {str(e)}")
            return render(request, "error.html", {"message": "Noma'lum xatolik yuz berdi."})

