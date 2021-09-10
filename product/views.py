from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.

class ProductList(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista de produto')

class ProductDetail(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe produto')


class AddToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adiciona do carrinh')


class RemoveToCart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remove do carrinho')


class Cart(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho1')


class Finish(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FIinish')
