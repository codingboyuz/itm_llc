from django.shortcuts import render
from django.views import View
from .models import AboutModel, CertificateModel

class AboutView(View):
    def get(self, request):
        try:
            data = AboutModel.objects.prefetch_related('image').all()
            certificate = CertificateModel.objects.all()


            print(f"data=================================================={certificate}")
            context = {
                "data": data,       # Matn, video va boshqa maydonlar
                "certificate":certificate
            }
            return render(request, "about.html", context)

        except Exception as e:
            return render(request, "error.html", {"message": f"Xatolik: {str(e)}"})
