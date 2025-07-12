from django.contrib import admin


from .models import AboutImage,AboutModel,CertificateModel


class AboutImageInline(admin.TabularInline):
    model = AboutImage
    extra =1


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display= ['title','description','video']
    inlines = [AboutImageInline]
    readonly_fields = ('created_at','updated_at')



@admin.register(CertificateModel)
class CertificateModelAdmin(admin.ModelAdmin):
    list_display= ['image']
