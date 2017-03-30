from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings


from apps.home.views import (
    LandingView, HomeView,
    ContactView, HelpView
    )

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LandingView.as_view(), name="landing"),
    url(r'^alfredynho/', ContactView.as_view(), name="contact_info"),


    url(r'^dashboard/$', HomeView.as_view(), name="dashboard"),
    # url(r'^integrations/', include('apps.messenger.urls', namespace="integrations")),

    # URL APPS PROJECT 
    url(r'^',include('apps.motorcycle.urls',namespace='motorcycle')),
    
    url(r'^',include('apps.replacement.urls', namespace='replacement')),

    url(r'^',include('apps.personal.urls', namespace='personal')),

    url(r'^',include('apps.usuario.urls', namespace='usuario')),

    url(r'^',include('apps.sale.urls', namespace='sale')),

    url(r'^',include('apps.assistant.urls',namespace='assistan')),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),

]	