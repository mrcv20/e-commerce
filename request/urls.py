from django.urls import path
from . import views

app_name = 'request'

urlpatterns = [
    path('', views.Pay.as_view(), name='pay'),
    path('closeorder', views.Pay.as_view(), name='close order'),
    path('detail', views.Pay.as_view(), name='detail'),
    
]
