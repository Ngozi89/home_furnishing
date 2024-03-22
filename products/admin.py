from django.contrib import admin
from .models import Product, Category, Color

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'itemnumber',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('itemnumber',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ColorAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Category, CategoryAdmin)