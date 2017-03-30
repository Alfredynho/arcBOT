from django.db import models
from django.utils.translation import ugettext_lazy as _

class Empresa(models.Model):
	nombre = models.CharField(
		verbose_name=_('Nombre Empresa'),
		max_length=150,
		blank=True,
		null=True
		)

	mision = models.CharField(
		verbose_name=_('Mision'),
		max_length=150,
		blank=True,
		null=True
		)

	vision = models.CharField(
		verbose_name=_('Vision'),
		max_length=150,
		blank=True,
		null=True
		)

	empleados = models.TextField(
		verbose_name=_('Empleados'),
		blank=True,
		null=True
		)

	direccion = models.TextField(
		verbose_name=_('Direccion'),
		blank=True,
		null=True
		)

	horarios = models.TextField(
		verbose_name=_('Horarios'),
		blank=True,
		null=True
		)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name=_('Informacion de la Sucursal')
		verbose_name_plural=_('Informacion de las Sucursales')