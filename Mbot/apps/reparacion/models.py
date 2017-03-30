from django.db import models
from django.utils.translation import ugettext_lazy as _
from apps.usuario.models import Usuario
from apps.personal.models import Personal
from apps.motorcycle.models import Motorcycle

class Reparacion(models.Model):
	placa = models.CharField(
		verbose_name=_('Placa Motocicleta'),
		max_length=50,
		unique=True
		)

	usuario = models.ForeignKey(
        'usuario.Usuario',
        on_delete=models.CASCADE,
		)

	motocicleta = models.ForeignKey(
		'motorcycle.Motorcycle',
		on_delete=models.CASCADE,
		)

	detalle_reparacion = models.TextField(
		verbose_name=_('Detalle de la reparacion'),
		blank=True,
		null=True,
		)

	personal = models.ForeignKey(
        'personal.Personal',
        on_delete=models.CASCADE,
		)

	inicio_reparacion = models.DateTimeField(
        verbose_name=_("Fecha de entrega al taller "),
		)

	fin_reparacion = models.DateTimeField(
        verbose_name=_("Fecha de Devolucion al usuario"),
		)

	def __str__(self):
		return "%s - %s" % (self.placa, self.motocicleta)

	class Meta:
		verbose_name=_('Reparacion de Motocicleta')
		verbose_name_plural=_('Reparacion de Motocicletas')