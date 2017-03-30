from django.views.generic import ListView, TemplateView,View
from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage, PageNotAnInteger

from apps.personal.models import Personal

def personal_view(request,pagina):
	personal_list = Personal.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(personal_list, 12)
	try:
		personal = paginator.page(page)
	except PageNotAnInteger:
		personal = paginator.page(1)
	except EmptyPage:
		personal = paginator.page(paginator.num_pages)
	context = {'personal':personal}
	return render(request,'personal/listar_personal.html',context)