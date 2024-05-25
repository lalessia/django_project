from django.db import models

#model field references: https://docs.djangoproject.com/en/5.0/ref/models/fields/
#making query: https://docs.djangoproject.com/en/5.0/topics/db/queries/

#Create Journalist models
class Journalist(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name} {self.first_name}"

# Create Article models
class Article(models.Model):
    """Modello generico per un Articolo di news"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    #NB settando il parametro on_delete=models.CASCADE, diciamo di cancellare tutti gli articoli a esso assegnati
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles") 


    def __str__(self):
        return self.title
