#this file has created manually for avoid every path depends from first_project/urls.py

from django.urls import path
from first_app import views as fa_views

urlpatterns = [
    path("home/", fa_views.home, name="home"),
    path("view_b/", fa_views.view_b, name="view_b"),
    path("view_c/", fa_views.view_c, name="view_c"),
]