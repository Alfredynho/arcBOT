from django.db import models
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
	name = models.CharField(
		verbose_name =_('Nombre'),
		max_length =150,
		null =True,
		blank =True,
		)

	description = models.TextField(
		verbose_name = _('Descripcion'),
		blank=True,
		null=True,
		)

	active = models.BooleanField(
		verbose_name=_('Activo'),
		default=True,
		)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name=_('Tipo de Categoria')
		verbose_name_plural=_('Tipo de Categorias')


class Assistant(models.Model):
	question = models.CharField(
		verbose_name =_('Pregunta'),
		blank = True,
		null = True,
		max_length= 180,		
		)

	answer = models.TextField(
		verbose_name=_('Respuesta'),
		null=True,
		blank=True,
		)

	category = models.ForeignKey(
		Category,
		verbose_name=_('Categoria'),
		)

	def __str__(self):
		return self.question

	class Meta:
		verbose_name=_('Asistencia del BOT')		
		verbose_name_plural=_('Asistencias del BOT')		



