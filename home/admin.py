# home/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import HomeModel

@admin.register(HomeModel)
class HomeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'info','image_preview')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'sub_title')
    list_filter = ('title',)
    readonly_fields = ('image_preview',)

    fieldsets = (
        (None, {
            'fields': ('title', 'sub_title','info')
        }),
        ('Image', {
            'fields': ('image', 'image_preview'),
        }),
    )

    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
