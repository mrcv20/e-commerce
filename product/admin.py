from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

class AdminProduct(admin.ModelAdmin):
    list_display = ['name']
    inlines = [
        VariationInline
    ]


admin.site.register(Product, AdminProduct)
admin.site.register(Variation)