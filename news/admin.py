from django.contrib import admin
from .models import NewsModel,NewsImages
# Register your models here.



class NewsImagesInline(admin.TabularInline):
    model = NewsImages
    extra =1


@admin.register(NewsModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display= ['title','description','slug']
    inlines = [NewsImagesInline]

