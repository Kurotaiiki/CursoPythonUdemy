from tabnanny import verbose
from django.db import models

# Create your models here.

class Post(models.Model):
    tittle= models.CharField(max_length=200,verbose_name="Titulo")
    content= models.TextField(verbose_name="Contenido")

    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"

    def __str__(self):
        return self.tittle

