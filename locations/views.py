from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


# def update_mo
