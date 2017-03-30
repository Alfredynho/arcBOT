# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import (
        RepuestoView, 
        NewRepuestoView,
        DetailRepuestoView,
        EditRepuestoView,
        DeleteRepuestoView
    )

urlpatterns = [
    url(
        regex=r'^repuestos/$',
        view=RepuestoView.as_view(),
        name='view-repuestos'
    ),

    url(
        regex=r'^nueva_repuesto/$',
        view=NewRepuestoView.as_view(),
        name='view-new-repuesto'
    ),


    url(
        regex=r'^(?P<pk>\d+)/$',
        view=DetailRepuestoView.as_view(),
        name='view-detail-repuesto'
    ),

    url(
        regex=r'^editar_repuesto/(?P<pk>\d+)/$',
        view=EditRepuestoView.as_view(),
        name='view-edit-repuesto'
    ),

    url(
        regex=r'^borrar_repuesto/(?P<pk>\d+)/$',
        view=DeleteRepuestoView.as_view(),
        name='view-delete-repuesto'
    ),

]
 