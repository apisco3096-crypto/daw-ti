from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta hace que al entrar a /portfolio/ se ejecute la vista que creamos
    path('', views.portfolio, name="portfolio"),
]
