from django.views.generic import ListView, TemplateView,View
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage, PageNotAnInteger

from apps.assistant.models import Assistant

class AsistenciaView(ListView):
	model = Assistant
	template_name = "asistencia/asistencia.html"
