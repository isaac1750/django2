from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from .models import Nav


class HomeView(TemplateView):
    template_name = "home.html"
