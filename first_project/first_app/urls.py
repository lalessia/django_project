#this file has created manually for avoid every path depends from first_project/urls.py

from django.urls import path
from first_app import views as fa_views
from first_app.views import article_detail_view, home, view_b, view_c

urlpatterns = [
    path("home/", home, name="home"),
    path("view_b/", view_b, name="view_b"),
    path("view_c/", view_c, name="view_c"),
    path("articles/<int:pk>/", article_detail_view, name="art_detail"),
]