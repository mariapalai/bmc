from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Canvas, Company
from django.views.generic.edit import CreateView

class CanvasList(ListView):
    model = Canvas

class CanvasDetailView(DetailView):
    model = Canvas

class CanvasCreate(CreateView):
    model = Canvas
    fields = ['name','value_propositions','customer_segments',
              'partners','relationships','channels','activities',
              'resources','revenue','cost']

class CompanyDetailView(DetailView):
    model = Company
