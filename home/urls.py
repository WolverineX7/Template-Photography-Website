from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('photo_detail_clock/', views.photo_detail_clock),
    path('about/', views.about),
    path('contact/', views.contact),
    path('contact/contact', views.contact),
    path('photo_detail_plant/', views.photo_detail_plant),
    path('photo_detail_morning/', views.photo_detail_morning),
    path('photo_detail_perfume/', views.photo_detail_perfume),
    path('photo_detail_headphone/', views.photo_detail_headphone),
    path('photo_detail_moon/', views.photo_detail_moon),
    path('photo_detail_bus/', views.photo_detail_bus),
    path('photo_detail_abstract/', views.photo_detail_abstract),
    path('photo_detail_flower/', views.photo_detail_flower),
    path('photo_detail_rosy/', views.photo_detail_rosy),
    path('photo_detail_rock/', views.photo_detail_rock),
    path('photo_detail_purple/', views.photo_detail_purple),
    path('photo_detail_sea/', views.photo_detail_sea),
    path('photo_detail_turtle/', views.photo_detail_turtle),
    path('photo_detail_peace/', views.photo_detail_peace),
    path('photo_detail_newyork/', views.photo_detail_newyork),
]
