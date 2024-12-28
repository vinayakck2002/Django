from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
      path('',views.signin,name='signin'),
      path('signup',views.usersignup,name='signup'),
      path('helo',views.index,name='hlw'),

    
]
