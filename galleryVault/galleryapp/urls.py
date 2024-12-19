from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.viewsmain,name='namemain'),
    path('delete/<pk>',views.delete,name='urdelete')

    ]

# This line ensures media files are served during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
