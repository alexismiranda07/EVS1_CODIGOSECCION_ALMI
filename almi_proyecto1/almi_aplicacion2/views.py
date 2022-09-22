from django.shortcuts import render
from django.http import HttpResponse
from almi_aplicacion2 import views
# Create your views here.
def video(request):
    return HttpResponse ('<a href="https://www.youtube.com/watch?v=d9BF1JvzE7I&ab_channel=robohobosam">motivacion</a>')

# Create your views here.
