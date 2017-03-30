from django.views.generic import ListView, TemplateView,View
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage, PageNotAnInteger

from apps.usuario.models import Usuario

def usuario_view(request,pagina):
	usuario_list = Usuario.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(usuario_list, 12)
	try:
		usuario = paginator.page(page)
	except PageNotAnInteger:
		usuario = paginator.page(1)
	except EmptyPage:
		usuario = paginator.page(paginator.num_pages)
	context = {'usuario':usuario}
	return render(request,'user/listar_usuario.html',context)