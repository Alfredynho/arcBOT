from django.conf.urls import include, url
from .views import personal_view

urlpatterns = [
	url(r'^personal/page/(?P<pagina>.*)/$',personal_view,name='vista_personal'),
]
 