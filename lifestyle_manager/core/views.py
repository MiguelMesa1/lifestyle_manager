from django.shortcuts import render
from django.utils import timezone
from habits.views import dashboard
# Create your views here.
from django.utils import timezone


def obtener_hora():
    return timezone.now()


def home(request):
    if request.user.is_authenticated:
        return dashboard(request)

    hora = obtener_hora()

    return render(request,'home/home.html', {
        'hora': hora
    })



