from django.shortcuts import render
from django.views import View
from .models import AboutModel, AboutImage

class AboutView(View):
    def get(self, request):
        try:
            data = AboutModel.objects.all()
            images = AboutImage.objects.select_related('about').all()

            context = {
                "data": data,       # Matn, video va boshqa maydonlar
                "images": images    # Alohida rasm obyektlari
            }
            return render(request, "about.html", context)

        except Exception as e:
            return render(request, "error.html", {"message": f"Xatolik: {str(e)}"})
