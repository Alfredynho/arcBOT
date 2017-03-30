from django.contrib import admin
from .models import Motorcycle, CreateType

@admin.register(Motorcycle)
class MotorcycleAdmin(admin.ModelAdmin):
	list_display =['id','serial_code','brand']

	class Meta:
		model = Motorcycle


@admin.register(CreateType)
class CreateTypeAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

	class Meta:
		model = CreateType