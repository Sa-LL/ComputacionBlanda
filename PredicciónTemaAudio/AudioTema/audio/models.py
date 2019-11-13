from django.db import models

# Create your models here.


class Audio(models.Model):
    nombre = models.CharField(max_length=120, default="Ninguno")
    audio = models.FileField()
    textoAudio = models.TextField()
    tema = models.CharField(max_length=120)


    def __str__(self):
        return f"{self.id} {self.nombre}"