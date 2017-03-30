from django.views.generic import ListView, TemplateView,View
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage, PageNotAnInteger

from apps.sale.models import VentaMotocicleta, VentaRepuesto

def venta_moto_view(request,pagina):
	venta_moto_list = VentaMotocicleta.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(venta_moto_list, 5)
	try:
		v_moto = paginator.page(page)
	except PageNotAnInteger:
		v_moto = paginator.page(1)
	except EmptyPage:
		v_moto = paginator.page(paginator.num_pages)
	context = {'motocicletas':v_moto}
	return render(request,'venta/venta_motocicletas.html',context)


def venta_repuesto_view(request,pagina):
	venta_repuesto_list = VentaRepuesto.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(venta_repuesto_list, 5)
	try:
		v_repuesto = paginator.page(page)
	except PageNotAnInteger:
		v_repuesto = paginator.page(1)
	except EmptyPage:
		v_repuesto = paginator.page(paginator.num_pages)
	context = {'repuestos':v_repuesto}
	return render(request,'venta/venta_repuestos.html',context)
