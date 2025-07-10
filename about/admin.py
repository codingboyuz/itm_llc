from django.contrib import admin


from .models import AboutImage,AboutModel


class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra =1


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display= ['title','description','video']
    inlines = [AboutImageInline]