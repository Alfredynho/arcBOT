from django.db import models
from django.utils.translation import ugettext_lazy as _

GENERAL = "GENERAL"
PAYMENTS = "PAYMENTS"
ACCOUNTS = "ACCOUNTS"
BOTS = "BOTS"
SUBSCRIPTIONS = "SUBSCRIPTIONS"
WEB = "WEB"

SECURITY = "SECURITY"
MOBILE = "MOBILE"

QUESTION_TYPES = (
  (GENERAL, _("Información General")),
  (WEB, _("Plataforma Web")),
  (MOBILE, _("Aplicación móvil")),
  (SECURITY, _("Accesos")),
  (PAYMENTS, _("Pagos")),
  (ACCOUNTS, _("Cuentas")),
  (SECURITY, _("Seguridad")),
  (BOTS, _("Bots")),
  (SUBSCRIPTIONS, _("Suscripciones")),
)


class Question(models.Model):

    user = models.ForeignKey(
        'usuario.Usuario',
        verbose_name=_("Usuario"),
    )

    category = models.CharField(
        verbose_name=_("Categoria"),
        choices=QUESTION_TYPES,
        default=GENERAL,
        max_length=50,
    )

    question = models.TextField(
        verbose_name=_('Pregunta'),
    )

    answer = models.TextField(
        verbose_name=_('Respuesta'),
    )

    def __str__(self):
        return self.question


class Suggestion(models.Model):

    user = models.ForeignKey(
        'usuario.Usuario',
        verbose_name=_("Usuario"),
    )

    subject = models.CharField(
        verbose_name=_('Asunto'),
        max_length=150,
    )

    message = models.TextField(
        verbose_name=_('Mensaje'),
    )

    date = models.DateField(
        verbose_name=_('Fecha de publicación'),
        auto_now=True,
    )

    def __str__(self):
        return self.subject