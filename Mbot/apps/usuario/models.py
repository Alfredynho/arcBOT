from django.db import models
from django.utils.translation import ugettext_lazy as _

class Usuario(models.Model):

	cedula = models.CharField(
		verbose_name =_("Cedula"),
		max_length = 50,
		blank = True,
		null = True,
		unique=True,
		)

	nombre = models.CharField(
		verbose_name =_("Nombre") ,
		max_length = 150,
		blank = True,
		null = True
		)

	paterno = models.CharField(
		verbose_name =_("Paterno"),
		max_length = 150,
		blank = True,
		null = True
		)

	materno = models.CharField(
		verbose_name =_("Materno"),
		max_length = 150,
		blank = True,
		null = True
		)

	celular = models.CharField(
		verbose_name =_("Celular"),
		max_length = 50,
		blank = True,
		null = True
		)


	def __str__(self):
		return "%s %s: " % (self.nombre, self.paterno)

	class Meta:
		verbose_name = _('Usuario')
		verbose_name_plural = _('Usuarios')