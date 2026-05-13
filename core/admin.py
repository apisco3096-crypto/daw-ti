from django.contrib import admin
from .models import Portafolio # Importamos tu clase Portafolio

# Configuramos cómo se verá en el panel
class PortafolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update') # Campos que no se pueden editar manualmente

admin.site.register(Portafolio, PortafolioAdmin)