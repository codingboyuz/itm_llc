from django.views import View
from django.shortcuts import render
from .models import PartnersModel
from product.models import ProductModel
from about.models import AboutModel

import logging

logger = logging.getLogger(__name__)

class HomePage(View):
    def get(self, request):
        try:
            partners = PartnersModel.objects.all()
            products = ProductModel.objects.prefetch_related("images").order_by('?')[:6]
            news = ProductModel.objects.all().first()
            about = AboutModel.objects.all().first()

            print(f"news=================={news}")
            print(f"products=================={products}")
            print(f"partners=================={partners}")
            print(f"about=================={about.title}")

            if news and about:
                context = {
                    'partners': partners,
                    'products': products,
                    'news': news,
                    'about': about,
                }
                # ❗ MUHIM: 'data' deb emas, to'g'ridan-to'g'ri context ni uzatamiz
                return render(request, "home.html", context)

            return render(request, "404.html", {"message": "Ma'lumot topilmadi!"})
        except Exception as e:
            logger.error(f"Home sahifasida xatolik: {str(e)}")
            return render(request, "error.html", {"message": "Noma'lum xatolik yuz berdi."})
