from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>¡Bienvenido a mi sitio!</h1>")  