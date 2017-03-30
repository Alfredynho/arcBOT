from django.db import models
from django.utils.translation import ugettext_lazy as _

class Promociones(models.Model):
	nombre = models.CharField(
		verbose_name=_('Nombre Promocion'),
		max_length=200,
		blank=True,
		null=True
		)

	descripcion = models.TextField(
		verbose_name=_('Descripcion'),
		help_text=_('Maximo de caracteres 126'),
		blank=True,
		null=True
		)

	fechas_promocion = models.TextField(
		verbose_name=_('Tiempo de la promocion'),
		help_text=_('Maximo de caracteres 90'),
		blank=True,
		null=True
		)

	imagen = models.ImageField(
		verbose_name=_('Imagen'),
		upload_to='imagenes/promociones/%Y/%m/%d',
		null=True,
		blank=True,
	)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name = _('Promocion')
		verbose_name_plural = _('Promociones')