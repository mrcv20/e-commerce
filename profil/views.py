from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Create(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Create')

class Update(View):
    def get(self, *args, **kwargs):
        return HttpResponse('UPdate')

class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')