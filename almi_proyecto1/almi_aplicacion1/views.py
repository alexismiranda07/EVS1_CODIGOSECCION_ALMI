from django.shortcuts import render
from django.http import HttpResponse
from almi_aplicacion1 import views
# Create your views here.
def display(request):
    return HttpResponse ("<h1>prueba</h1>")
def video(request):      
    return HttpResponse ('<a href="https://youtu.be/ik3o5VU74aA?t=280">Danger link</a>')