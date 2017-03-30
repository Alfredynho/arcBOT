from django.contrib import admin
from .models import VentaMotocicleta , VentaRepuesto

@admin.register(VentaMotocicleta)
class VentaMotoAdmin(admin.ModelAdmin):
	list_display = ['motocicleta', 'usuario', 'personal','fecha', 'cantidad', 'total']

	class Meta:
		models = VentaMotocicleta

@admin.register(VentaRepuesto)
class VentaRepuestoAdmin(admin.ModelAdmin):
	list_display = ['repuesto', 'usuario', 'personal','fecha', 'cantidad', 'total']

	class Meta:
		models = VentaRepuesto
