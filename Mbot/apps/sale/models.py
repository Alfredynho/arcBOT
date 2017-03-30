from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.motorcycle.models import Motorcycle
from apps.replacement.models import Repuesto
from apps.usuario.models import Usuario
from apps.personal.models import Personal

class VentaMotocicleta(models.Model):
	
	motocicleta = models.ForeignKey(
		'motorcycle.Motorcycle'
		)

	usuario = models.ForeignKey(
		'usuario.Usuario'
		)

	personal = models.ForeignKey(
		'personal.Personal'
		)

	fecha = models.DateTimeField(
		verbose_name=_('Fecha de Venta')
		)

	cantidad = models.PositiveSmallIntegerField(
		verbose_name=_('Cantidad'),
		null = True, 
		default = 1,
	)

	total = models.FloatField(
		verbose_name='Monto a pagar',
		blank=True,
		null=True,
	)


	def __str__(self):
		return str(self.motocicleta)

	class Meta:
		verbose_name=_('Venta de Motocicleta')
		verbose_name_plural=_('Venta de Motocicletas')

class VentaRepuesto(models.Model):
	repuesto = models.ForeignKey(
		'replacement.Repuesto'
		)

	usuario = models.ForeignKey(
		'usuario.Usuario'
		)

	personal = models.ForeignKey(
		'personal.Personal'
		)

	fecha = models.DateTimeField(
		verbose_name=_('Fecha de Venta')
		)

	cantidad = models.PositiveSmallIntegerField(
		verbose_name=_('Cantidad'),
		null = True, 
		default = 1,
	)

	total = models.FloatField(
		verbose_name=_('Monto a pagar'),
		blank=True,
		null=True,
	)


	def __str__(self):
		return str(self.repuesto)

	class Meta:
		verbose_name=_('Venta de Repuesto')
		verbose_name_plural=_('Venta de Repuestos')