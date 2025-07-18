from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import handler404
from django.shortcuts import render

# 404 xatolik bo‘lsa chaqiriladigan view
def custom_404(request, exception):
    return render(request, '404.html', status=404)

# handler nomini belgilang
handler404 = custom_404

urlpatterns = [path('admin/', admin.site.urls),
]
urlpatterns += i18n_patterns(
    path('i18n/',include('django.conf.urls.i18n')),
    path('', RedirectView.as_view(url='/uz/home/', permanent=False)),
    path('home/', include('home.urls')),
    path('products/', include('product.urls')),
    path('about/', include('about.urls')),
    path('news/', include('news.urls')),

)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)