from django.urls import path
from inicio.views import inicio, paletas, autos, crear_paleta, crear_auto, crear_moto, motos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('paletas/', paletas, name='paletas'),
    path('autos/', autos, name='autos'),
    path('paletas/crear/', crear_paleta, name='crear_paleta'),
    path('autos/crear/', crear_auto, name='crear_auto'),
    path('motos/crear/', crear_moto, name='crear_moto'),
    path('motos/', motos, name='motos')
]
