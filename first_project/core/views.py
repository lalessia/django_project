from django.shortcuts import render
from core.views import home

def home(request):
    return HttpResponse(f"<h1>Homepage Core app!</h1>")
