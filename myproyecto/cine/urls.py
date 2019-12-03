from django.contrib import admin
from django.urls import path,include 
from .views import index, gale, quienes_somos,formulario

urlpatterns = [
    path('', index,name='IND'),
    path('galeria/',gale,name='GAL'),
    path('formulario/',formulario,name='FORMU'),
    path('quienes_somos/',quienes_somos,name='QUIEN'),
]
