from django.shortcuts import redirect, render, get_object_or_404
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Habito

# Renderiza el dashboard
@login_required
def dashboard(request):
    return render(request, "habits/dashboard.html") 

# Listar Todos Los Hábitos Por Usuario
@login_required
def listar_habitos(request):
    habitos = Habito.objects.filter(usuario=request.user)
    return render(request, "habits/habits.html", {"habitos": habitos})

# Hábitos que corresponder a la fecha en la que se encuentra el usuario. 
@login_required
def habitos_diarios(request):
    pass

# Crear Hábito
@login_required
def crear_habito(request):

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        evento = request.POST.get("evento")
        frecuencia = request.POST.get("frecuencia")
        lunes = request.POST.get("lunes") == "on"
        martes = request.POST.get("martes") == "on"
        miercoles = request.POST.get("miercoles") == "on"
        jueves = request.POST.get("jueves") == "on"
        viernes = request.POST.get( "viernes") == "on"
        sabado = request.POST.get("sabado") == "on"
        domingo = request.POST.get("domingo") == "on"

        Habito.objects.create(
            usuario=request.user,
            nombre=nombre,
            evento=evento,
            frecuencia=frecuencia,
            lunes=lunes,
            martes=martes,
            miercoles=miercoles,
            jueves=jueves,
            viernes=viernes,
            sabado=sabado,
            domingo=domingo   
        )

        return redirect("listar_habitos")

    return redirect("listar_habitos")

# Actualizar hábito
@login_required
def editar_habito(request, id):
    habito = get_object_or_404(
        Habito,
        id=id,
        usuario=request.user
    )

    if request.method == "POST":
        habito.nombre = request.POST.get("nombre")
        habito.evento = request.POST.get("evento")
        habito.frecuencia = request.POST.get("frecuencia")

        habito.lunes = request.POST.get("lunes") == "on"
        habito.martes = request.POST.get("martes") == "on"
        habito.miercoles = request.POST.get("miercoles") == "on"
        habito.jueves = request.POST.get("jueves") == "on"
        habito.viernes = request.POST.get("viernes") == "on"
        habito.sabado = request.POST.get("sabado") == "on"
        habito.domingo = request.POST.get("domingo") == "on"

        habito.save()

        return redirect("listar_habitos")

    habitos = Habito.objects.filter(usuario=request.user)

    return render(request, "habits/habits.html",{"habito": habito,"habitos": habitos})
#Eliminar Hábito

@login_required
@require_POST
def eliminar_habito(request, id):
        habito = get_object_or_404(Habito, id=id, usuario = request.user)

        habito.delete()

        return redirect("listar_habitos")


