from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Canvas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render_to_response


def company(request, pk):
    try:
        obj = Canvas.objects.get(pk=pk)
    except Canvas.DoesNotExist:
        raise Http404("Canvas does not exist")
    return render_to_response('app/company_detail.html', {'obj': obj})


class CanvasList(ListView):
    model = Canvas


class CanvasDetailView(DetailView):
    model = Canvas


class CanvasCreate(CreateView):
    model = Canvas
    fields = ['company','value_propositions','customer_segments',
              'partners','relationships','channels','activities',
              'resources','revenue','cost', 'description', 'logo']


class CanvasUpdate(UpdateView):
    model = Canvas
    fields = ['company','value_propositions','customer_segments',
              'partners','relationships','channels','activities',
              'resources','revenue','cost', 'description', 'logo']


class CanvasDelete(DeleteView):
    model = Canvas
    success_url = reverse_lazy('canvas-list')

