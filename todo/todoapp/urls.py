from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

  path('',views.add_todo,name="add_todo"),
  path('delete_g/<int:pk>',views.delete_g,name='delete_g'),
]