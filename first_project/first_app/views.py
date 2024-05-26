from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from first_app.models import Journalist, Article

#https://docs.djangoproject.com/en/5.0/ref/templates/
def home(request):
    articles = Article.objects.all()
    journalists = Journalist.objects.all()
    context={"articles": articles, "journalists": journalists}
    return render(request, "first_app/home.html", context)

def article_detail_view(request, pk):
    #Alternativa a usare la classe get_object_or_404, soltanto che non permette la gestione delle pagine d'errore
    #article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    context = {"article": article}
    return render(request, "first_app/detail_view.html", context)

def view_b(request):
    return HttpResponse("<h1>Ciao a tutti! Sono la view_b</h1>")

def view_c(request):
    return HttpResponse("<h1>Ciao a tutti! Sono la view_c</h1>")

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
