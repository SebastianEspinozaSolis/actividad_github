from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('primeraView/',views.primeraView),
    path('segundaView/',views.segundaView),
]