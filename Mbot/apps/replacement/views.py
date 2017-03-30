from django.views.generic import ListView, TemplateView,View
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage, PageNotAnInteger

from apps.replacement.models import Repuesto

def repuesto_view(request,pagina):
	repuesto_list = Repuesto.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(repuesto_list, 5)
	try:
		repuestos = paginator.page(page)
	except PageNotAnInteger:
		repuestos = paginator.page(1)
	except EmptyPage:
		repuestos = paginator.page(paginator.num_pages)
	context = {'repuestos':repuestos}
	return render(request,'productos/repuestos/listar_repuestos.html',context)