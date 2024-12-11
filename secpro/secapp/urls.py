from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
 path('',views.index,name='index'),
 path('index2',views.index2,name='index2'),
 path('index3',views.index3,name='index3'),
 path('index4',views.index4,name='index4'),
]
