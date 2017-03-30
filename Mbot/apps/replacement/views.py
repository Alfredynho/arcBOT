from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView ,DeleteView ,ListView ,TemplateView ,UpdateView ,DetailView

from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage, PageNotAnInteger
from django.contrib import messages

from .models import Repuesto
from .forms import RepuestoForm


class RepuestoView(ListView):
    template_name = "productos/repuestos/listar_repuestos.html"
    model = Repuesto
    context_object_name = "repuestos"

    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super(RepuestoView, self).get_context_data(**kwargs) 
        list_repuestos = Repuesto.objects.all()
        paginator = Paginator(list_repuestos, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            list_repuestos = paginator.page(page)
        except PageNotAnInteger:
            list_repuestos = paginator.page(1)
        except EmptyPage:
            list_repuestos = paginator.page(paginator.num_pages)

        context['list_repuestos'] = list_repuestos
        return context


class NewRepuestoView(CreateView):
    template_name = "productos/repuestos/new_repuesto.html"
    model = Repuesto
    form_class = RepuestoForm
    
    def get_success_url(self):
        messages.info(self.request,"Repuesto creado con exito")
        return reverse_lazy("replacement:view-repuestos")


class EditRepuestoView(UpdateView):
    template_name = "productos/repuestos/update_repuesto.html"
    model = Repuesto
    form_class = RepuestoForm

    def get_success_url(self):
        messages.info(self.request,"Repuesto modificado con exito")
        return reverse_lazy("replacement:view-repuestos")

class DetailRepuestoView(DetailView):
    model = Repuesto
    success_url = reverse_lazy("replacement:view-repuestos")

class DeleteRepuestoView(DeleteView):
    model = Repuesto
    template_name = "productos/repuestos/repuesto_delete.html"

    def get_success_url(self):
        messages.info(self.request,"Repuesto Eliminado con exito")
        return reverse_lazy("replacement:view-repuestos")


