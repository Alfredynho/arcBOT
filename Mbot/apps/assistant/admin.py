from django.contrib import admin
from .models import Assistant , Category

@admin.register(Assistant)
class AsistantAdmin(admin.ModelAdmin):
	list_display = ['id', 'question','answer','category']

	class Meta:
		model = Assistant

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','description','active']

	class Meta:
		model = Category