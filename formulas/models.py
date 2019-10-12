from django.db import models

class Formulas(models.Model):
    nombre = models.CharField(max_length=250)
    fomula = models.CharField(max_length=250)
    def __str__(self):
        return self.nombre
