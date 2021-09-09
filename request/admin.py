from django.contrib import admin
from .models import Request, RequestItem

# Register your models here.

class RequestItemInline(admin.TabularInline):
    model = RequestItem
    extra = 1

class AdminRequest(admin.ModelAdmin):
    inlines = [
        RequestItemInline
    ]



admin.site.register(Request, AdminRequest)
admin.site.register(RequestItem)