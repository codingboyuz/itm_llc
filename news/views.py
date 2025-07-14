from django.shortcuts import render,get_object_or_404
from django.views import View
# Create your views here.

from .models import NewsModel
from shared.utils import log_request

class NewsView(View):
    def get(self,request):
        log_request(logger_name="news",request=request)
        try:
            data = NewsModel.objects.prefetch_related("images").all()
            print(f"news==========================={data}")
            if data.exists():
                context = {"data":data}

                return render(request,'news.html',context)
            
            return render(request, "404.html", {"message": "Ma'lumot topilmadi!"})            
        except Exception as e:
            print(f"news==========================={e}")

            return render(request, "error.html", {"message": f"Xatolik: {str(e)}"})


class NewsDetailView(View):
    def get(self, request, slug):
        log_request(logger_name="news_detail",request=request)

        try:
            news = get_object_or_404(NewsModel.objects.prefetch_related("images"), slug=slug)
            context = {
                "object": news,
            }
            return render(request, "news_detail.html", context)
        
        except Exception as e:
            print(f"NewsDetailView error: {e}")
            return render(request, "error.html", {"message": f"Xatolik: {str(e)}"})
