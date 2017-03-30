from django.db import models
from django.utils.translation import ugettext_lazy as _

class CreateType(models.Model):
	name = models.CharField(
		verbose_name=_('Tipo'),
		blank=True,
		null= True,
		max_length=100,
		unique=True,
	)	

	def __str__(self):
		return self.name

	class Meta:
		verbose_name=_('Tipo de Motocicleta')
		verbose_name_plural = _('Tipos de motocicleta')


class Motorcycle(models.Model):
	serial_code = models.CharField(
		verbose_name=_('Codigo Motocicleta'),
		null=True, 
		blank=True, 
		max_length=100,
		unique=True,
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

	color = models.CharField(
		verbose_name=_('Color'),
		null=True, 
		blank=True, 
		max_length=100,
	)

	price = models.FloatField(
		verbose_name=_('Precio'),
		null=True, 
		blank=True,
	)

	cylinder_capacity = models.CharField(
		verbose_name=_('Cilindrada'),
		null = True,
		max_length=100, 
		blank=True,
	)

	model = models.CharField(
		verbose_name=_('Modelo'),
		null=True, 
		blank=True, 
		max_length=100,
		)

	box = models.CharField(
		verbose_name=_('Caja'),
		null=True, 
		blank=True, 
		max_length=100,
		)

	motor = models.CharField(
		verbose_name=_('Motor'),
		null=True,
		blank=True,
		max_length=200,
		)

	characteristics = models.TextField(
		verbose_name=_('Caracteristicas'),
		null=True, 
		blank=True,
	)

	type = models.ForeignKey(
		CreateType,
		verbose_name=_('Tipo')
	)


	image = models.ImageField(
		verbose_name=_('Imagen'),
		upload_to='imagenes/motocicletas/%Y/%m/%d',
		null=True,
		blank=True,
	)


	def __str__(self):
		return "%s %s: " % (self.serial_code, self.brand)

	class Meta:
		verbose_name=_('Motocicleta')
		verbose_name_plural=_('Motocicletas')
