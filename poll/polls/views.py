from django.shortcuts import render
from djago.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, World")