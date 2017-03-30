from django.shortcuts import render

from django.views.generic import TemplateView

class LandingView(TemplateView):
	template_name = "landing.html"

class HomeView(TemplateView):
	template_name = "home/home.html"


class ContactView(TemplateView):
	template_name = "help/inf_contact.html"


class HelpView(TemplateView):
	template_name = "help_system.html"
