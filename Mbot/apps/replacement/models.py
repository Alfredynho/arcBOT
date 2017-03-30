from django.db import models
from django.utils.translation import ugettext_lazy as _

class Repuesto(models.Model):
	serial_code = models.CharField(
		verbose_name=_('Codigo Repuesto'),
		null=True, 
		blank=True, 
		max_length=100,
		unique=True,
	)

	name = models.CharField(
		verbose_name=_('Nombre del Repuesto'),
		null=True, 
		blank=True, 
		max_length=100,
	)

	description = models.TextField(
		verbose_name=_('Descripcion'),
		help_text='Cantidad maxima de caracteres 120',
		null=True, 
		blank=True,
	)

	stock = models.PositiveSmallIntegerField(
		verbose_name=_('Cantidad'),
		null = True, 
		default = 0,
	)

	brand = models.CharField(
		verbose_name=_('Marca'),
		null=True, 
		blank=True, 
		max_length=100,
		default='USM',
	)

	price = models.FloatField(
		verbose_name=_('Precio'),
		null=True, 
		blank=True,
	)

	image = models.ImageField(
		verbose_name=_('Imagen'),
		upload_to='imagenes/repuestos/%Y/%m/%d',
		null=True,
		blank=True,
	)


	def __str__(self):
		return "%s %s: " % (self.serial_code, self.name)

	class Meta:
		verbose_name=_('Repuesto')
		verbose_name_plural=_('Repuestos')
