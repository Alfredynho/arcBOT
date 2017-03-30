from django.contrib import admin
from .models import Promociones

@admin.register(Promociones)
class PromocionesAdmin(admin.ModelAdmin):
	list_display =['id','nombre','descripcion','fechas_promocion', 'imagen']

	class Meta:
		model = Promociones

