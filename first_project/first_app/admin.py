from django.contrib import admin
from first_app.models import Article, Journalist

#con le seguenti righe di codice gestiamo nella pagina admin del nostro sito i modelli, Article e Journalist, come se fossero all'interno di un db locale
admin.site.register(Article)
admin.site.register(Journalist)
