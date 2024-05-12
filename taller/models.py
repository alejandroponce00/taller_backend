from django.db import models

class Task(models.Model):
    vehiculo = models.CharField(max_length=200)
    dueño = models.CharField(max_length=200)
    falla = models.CharField(max_length=200)
    reparado = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
