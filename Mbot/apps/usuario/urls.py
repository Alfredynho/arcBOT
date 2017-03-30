from django.conf.urls import include, url
from .views import usuario_view

urlpatterns = [
	url(r'^usuario/page/(?P<pagina>.*)/$',usuario_view, name='vista_usuarios'),
]
 