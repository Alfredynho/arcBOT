from django.conf.urls import include, url
from .views import repuesto_view

urlpatterns = [
	url(r'^repuestos/page/(?P<pagina>.*)/$',repuesto_view,name='vista_repuestos'),
]
 