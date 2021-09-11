from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductList.as_view(), name='lista'),
    path('addtocart/', views.AddToCart.as_view(), name='adiciona'),
    path('rmtocart', views.RemoveToCart.as_view(), name='rmtocard'),
    path('cart', views.Cart.as_view(), name='cart'),
    path('finish', views.Finish.as_view(), name='finish'),
    path('<slug>/', views.ProductDetail.as_view(), name='detail'),
]
