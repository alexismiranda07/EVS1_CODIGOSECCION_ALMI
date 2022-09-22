from django.shortcuts import render
from django.http import HttpResponse
from almi_aplicacion2 import views
import datetime
# Create your views here.
def video(request):
    return HttpResponse ('<a href="https://www.youtube.com/watch?v=d9BF1JvzE7I&ab_channel=robohobosam">motivacion</a>')
def display(request):
    return HttpResponse ("<h1>ayuda tengo nervios</h1>") 
def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<b> la hora actualmente </b>" +str(dt)
    return HttpResponse(s)

