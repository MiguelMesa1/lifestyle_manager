from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

# Inicio de Sesión
def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:
            error = "Usuario o contraseña incorrectos."

    return render(
        request,
        "users/register.html",
        {
            "error": error
        }
    )


# Cerrar Sesión
@require_POST
def cerrar_sesion(request):
    logout(request)
    return redirect('home')