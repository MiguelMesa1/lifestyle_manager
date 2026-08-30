from django.urls import path
from . import views


urlpatterns = [
    path("habitos/", views.listar_habitos, name="listar_habitos"),
    path("crear/", views.crear_habito, name="crear_habito"),
    path("editar/<int:id>", views.editar_habito, name="editar_habito"),    
]