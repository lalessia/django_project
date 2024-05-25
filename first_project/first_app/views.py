from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Ciao a tutti! Sono la Home</h1>")

def view_b(request):
    return HttpResponse("<h1>Ciao a tutti! Sono la view_b</h1>")

def view_c(request):
    return HttpResponse("<h1>Ciao a tutti! Sono la view_c</h1>")
