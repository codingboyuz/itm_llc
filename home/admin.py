# home/admin.py

from django.contrib import admin

from .models import PartnersModel

@admin.register(PartnersModel)
class PartnersModelAdmin(admin.ModelAdmin):
    list_display= ['image']