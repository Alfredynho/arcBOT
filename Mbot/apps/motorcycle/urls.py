# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import (
        MotocicletaView, 
        NewMotorcycleView,
        DetailMotorcycleView,
        EditMotorcycleView,
        DeleteMotorcycleView
    )

urlpatterns = [
    url(
        regex=r'^motocicletas/$',
        view=MotocicletaView.as_view(),
        name='view-motocicletas'
    ),

    url(
        regex=r'^nueva_motocicleta/$',
        view=NewMotorcycleView.as_view(),
        name='view-new-motocicleta'
    ),


    url(
        regex=r'^(?P<pk>\d+)/$',
        view=DetailMotorcycleView.as_view(),
        name='view-detail-motocicleta'
    ),

    url(
        regex=r'^editar_motocicleta/(?P<pk>\d+)/$',
        view=EditMotorcycleView.as_view(),
        name='view-edit-motocicleta'
    ),

    url(
        regex=r'^borrar_motocicleta/(?P<pk>\d+)/$',
        view=DeleteMotorcycleView.as_view(),
        name='view-delete-motocicleta'
    ),

]
 