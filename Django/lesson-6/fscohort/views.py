from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse(request, '<h1>Welcome Django!</h1>')
