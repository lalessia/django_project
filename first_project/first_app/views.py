from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Journalist, Article

'''
home example

def home(request):
    articles = []
    journalists = []
    for a in Article.objects.all():
        articles.append(a.title)

    for j in Journalist.objects.all():
        journalists.append(j.first_name)

    response = str(articles) + "<br>" + str(journalists)
    print(response)

    return HttpResponse("<h1>Ciao a tutti! Sono la Home</h1>")
'''
#https://docs.djangoproject.com/en/5.0/ref/templates/
def home(request):
    articles = Article.objects.all()
    journalists = Journalist.objects.all()
    content={"articles": articles, "journalists": journalists}
    return render(request, "first_app/home.html", content)

def view_b(request):
    return HttpResponse("<h1>Ciao a tutti! Sono la view_b</h1>")

def view_c(request):
    return HttpResponse("<h1>Ciao a tutti! Sono la view_c</h1>")
