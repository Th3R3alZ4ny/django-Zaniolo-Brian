from pyexpat import model
from django.db import models

# Create your models here.
class Materie(models.Model):
    materia= models.CharField(max_length=20)
    
    def __str__(self):
        return self.materia

class Studenti(models.Model):
    materia=models.CharField(max_length=20)
    voti=models.IntegerField(_("2"))

    def __str__(self):
        return self.materia,self.voti