from django.shortcuts import render
from .models import Project  # Importante: Importar tu modelo

def portfolio(request):
    # Aquí obtenemos todos los proyectos que subiste al Admin
    projects = Project.objects.all()
    # Pasamos esos proyectos al HTML mediante el diccionario {'projects': projects}
    return render(request, "portfolio/portfolio.html", {'projects': projects})