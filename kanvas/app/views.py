from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Canvas, Company


class CanvasList(ListView):
    model = Canvas

class CanvasDetailView(DetailView):
    model = Canvas

class CompanyDetailView(DetailView):
    model = Company
