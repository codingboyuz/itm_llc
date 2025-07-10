#
from django.contrib import admin
from .models import ProductModel, ProductImage, ProductField,ProductCategory



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductFieldInline(admin.TabularInline):
    model = ProductField
    extra = 1
    fields = ()  # Avtomatik maydonlarni o'chirib qo'yamiz
    verbose_name_plural = "Product Fields"

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'created_at']
    inlines = [ProductImageInline, ProductFieldInline]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'verbose_name']