from django.conf.urls import include, url
from .views import venta_moto_view, venta_repuesto_view

urlpatterns = [
	url(r'^venta_motocicleta/page/(?P<pagina>.*)/$',venta_moto_view,name='vista_venta_moto'),
	url(r'^venta_repuesto/page/(?P<pagina>.*)/$',venta_repuesto_view,name='vista_venta_repuesto'),
]