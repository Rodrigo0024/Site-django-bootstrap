
# models.py
from django.db import models

class Anime(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    genero = models.CharField(max_length=50)
    
    
    # Adicione outros campos conforme necessário: data de lançamento, estúdio, etc.

    def __str__(self):
        return self.titulo