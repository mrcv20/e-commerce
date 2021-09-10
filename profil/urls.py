from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.Create.as_view(), name='Create'),
    path('update/', views.Update.as_view(), name='Update'),
    path('login/', views.Login.as_view(), name='Login'),
    path('logout/', views.Logout.as_view(), name='Logout'),
    
]
