from django.contrib import admin
from .models import Repuesto

@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
	list_display = ['id','name', 'serial_code', 'brand']

	class Meta:
		model = Repuesto