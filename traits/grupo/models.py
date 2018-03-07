from django.db import models
from persona.models import Persona
# Create your models here.
class grupo(models.Model):
    titulo = models.CharField(max_length=100)
    referencias = models.TextField(max_length=200)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    imagen = models.ImageField()