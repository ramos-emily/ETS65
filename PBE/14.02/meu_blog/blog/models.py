from django.db import models

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
