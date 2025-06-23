# C:\Practical\DjangoLaba5\DjangoLaba5_project\cars\admin.py

from django.contrib import admin
from .models import Dealership, TeslaCar # <<-- ПЕРЕВІРТЕ ІМПОРТ

@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone_number', 'email')
    search_fields = ('name', 'city', 'email')
    list_filter = ('city',)

@admin.register(TeslaCar)
class TeslaCarAdmin(admin.ModelAdmin):
    list_display = ('model', 'dealership', 'year', 'color', 'price', 'mileage', 'is_new', 'vin')
    list_filter = ('model', 'color', 'is_new', 'drivetrain', 'dealership__city')
    search_fields = ('model', 'vin', 'dealership__name')
    raw_id_fields = ('dealership',) # Зручніше для вибору дилерства
    fieldsets = (
        (None, {
            'fields': ('dealership', 'model', 'color', 'drivetrain', 'vin')
        }),
        ('Технічні характеристики', {
            'fields': ('year', 'battery_range_km', 'mileage'),
            'classes': ('collapse',)
        }),
        ('Продаж', {
            'fields': ('price', 'is_new')
        }),
    )