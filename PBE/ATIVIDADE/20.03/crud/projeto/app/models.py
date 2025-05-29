from django.db import models

class Evento(models.Model):
    name = models.CharField(max_length=30)
    Description = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    Location = models.TextField(max_length=100)
    Category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

        
    
