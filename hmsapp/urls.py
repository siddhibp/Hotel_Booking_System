from django.contrib import admin
from django.urls import path
from hmsapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create',views.create),
    path('dashboard',views.dashboard),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('',views.index),
    path('register/',views.register),
    path('login/',views.user_login),
    path('logout',views.user_logout),
    

    path('home/',views.home),
    path('contact/',views.contact),
    path('rooms/',views.rooms),
    path('book/',views.book)
    
 
    
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
     