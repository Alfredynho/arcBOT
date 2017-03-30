from django.contrib import admin
from .models import Reparacion

@admin.register(Reparacion)
class ReparacionAdmin(admin.ModelAdmin):
	list_display = ['id','placa', 'usuario', 'personal', 'motocicleta']

	class Meta:
		models = Reparacion
