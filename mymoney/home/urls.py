from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path("addmoney", views.addmoney, name='addmoney'),
    path('makeshop', views.makeshop, name='makeshop')
]
