#this file has created manually for avoid every path depends from first_project/urls.py

from django.urls import path
from core import views as c_views

urlpatterns = [
    path("asd/", c_views.home, name="home"),
]