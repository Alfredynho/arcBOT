from django.contrib import admin
from .models import Personal

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
	list_display =['id','nombre','paterno','materno', 'cedula', 'celular', 'cargo']

	class Meta:
		model = Personal

