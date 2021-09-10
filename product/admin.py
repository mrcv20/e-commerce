from django.contrib import admin
from .models import Product, Variation

# Register your models here.

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 1

class AdminRequest(admin.ModelAdmin):
    inlines = [
        VariationInline
    ]




admin.site.register(Product, AdminRequest)
admin.site.register(Variation)