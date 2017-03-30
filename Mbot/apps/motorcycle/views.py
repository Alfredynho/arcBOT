from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView ,DeleteView ,ListView ,TemplateView ,UpdateView ,DetailView

from django.shortcuts import render, render_to_response,redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator,EmptyPage,InvalidPage, PageNotAnInteger
from django.contrib import messages


from .models import Motorcycle
from .forms import MotorcycleForm

class MotocicletaView(ListView):
    template_name = "productos/motocicletas/listar_motocicletas.html"
    model = Motorcycle
    context_object_name = "motocicletas"

    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super(MotocicletaView, self).get_context_data(**kwargs) 
        list_motos = Motorcycle.objects.all()
        paginator = Paginator(list_motos, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            list_motos = paginator.page(page)
        except PageNotAnInteger:
            list_motos = paginator.page(1)
        except EmptyPage:
            list_motos = paginator.page(paginator.num_pages)

        context['list_motos'] = list_motos
        return context


class NewMotorcycleView(CreateView):
    template_name = "productos/motocicletas/new_motorcycle.html"
    model = Motorcycle
    form_class = MotorcycleForm
    
    def get_success_url(self):
        messages.info(self.request,"Motocicleta creada con exito")
        return reverse_lazy("motorcycle:view-motocicletas")


class EditMotorcycleView(UpdateView):
    template_name = "productos/motocicletas/update_motorcycle.html"
    model = Motorcycle
    form_class = MotorcycleForm

    def get_success_url(self):
        messages.info(self.request,"Motocicleta modificada con exito")
        return reverse_lazy("motorcycle:view-motocicletas")

class DetailMotorcycleView(DetailView):
    model = Motorcycle
    success_url = reverse_lazy("motorcycle:view-motocicletas")

class DeleteMotorcycleView(DeleteView):
    model = Motorcycle
    template_name = "productos/motocicletas/motorcycle_delete.html"

    def get_success_url(self):
        messages.info(self.request,"Motocicleta Eliminada con exito")
        return reverse_lazy("motorcycle:view-motocicletas")
