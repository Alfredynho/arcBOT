from django.conf.urls import include, url
from .views import AsistenciaView

urlpatterns = [
	url(r'^asistencia/$',AsistenciaView.as_view(),name='vista-asistencia'),
]
 