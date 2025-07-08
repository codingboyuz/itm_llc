# from django.contrib import admin
# from django.contrib import admin
# from django.utils.html import format_html
# from .models import ProductModel
#
#
#
# @admin.register(ProductModel)
# class ProductModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'description', 'category','image','created_at')
#     list_display_links = ('id', 'name')
#     search_fields = ('name', 'category')
#     list_filter = ('name',)
#     readonly_fields = ('image_preview',)
#
#     fieldsets = (
#         (None, {
#             'fields': ( 'name', 'description', 'category')
#         }),
#         ('Image', {
#             'fields': ('image', 'image_preview'),
#         }),
#     )
#
#     def image_preview(self, obj):
#         if obj.image and hasattr(obj.image, 'url'):
#             return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
#         return "-"
#
#
#     image_preview.short_description = 'Image Preview'
#
from django.contrib import admin
from .models import ProductModel, ProductImage, ProductField


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductFieldInline(admin.TabularInline):
    model = ProductField
    extra = 1


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_at']
    inlines = [ProductImageInline, ProductFieldInline]
