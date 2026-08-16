from django.shortcuts import render
from django.utils import timezone


# Create your views here.
from django.shortcuts import render
from django.utils import timezone


def obtener_hora():
    return timezone.now()


def home(request):
    hora = obtener_hora()

    return render(request, 'home/home.html', {
        'hora': hora
    })


