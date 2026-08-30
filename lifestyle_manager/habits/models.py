from django.db import models
from django.contrib.auth.models import User

class Habito(models.Model):

    FRECUENCIAS = [
        ("todos", "Todos los días"),
        ("dias", "Días específicos"),
    ]

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=100)  
    evento = models.TextField(blank=True)


    frecuencia = models.CharField(
        max_length=10,
        choices=FRECUENCIAS,
        default="todos"
    )

    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre