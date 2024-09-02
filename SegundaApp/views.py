from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Index de la segunda app</h1>")

def primeraView(request):
    html="""
    <h1 style="color:Purple">Titulo de la primera View</h1>
    <h2>Soy un subtitulo de la primera view, alojada en la Segunda app</h2>
    """
    return HttpResponse(html)

def segundaView(request):
    html="""
    <h1 style="color:Red">Titulo de la segunda View</h1>
    <h2>Soy un subtitulo de la segunda view, alojada en la Segunda app</h2>
    """
    return HttpResponse(html)