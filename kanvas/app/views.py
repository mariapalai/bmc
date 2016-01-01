from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Canvas
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from app.forms import CanvasForm


def company(request, pk):
    """
    This is function and not a generic view as it point to a different template from canvas_detail
    :param request:
    :param pk: primary key of Canvas as a named group of a regular expression at urls
    :return:
    """
    try:
        obj = Canvas.objects.get(pk=pk)
    except Canvas.DoesNotExist:
        raise Http404("Canvas does not exist")
    return render_to_response('app/company_detail.html', {'obj': obj})


def updateField(request, pk, field):
    """

    :param request:
    :param pk: primary key of Canvas
    :param field: which field to update
    :return:
    """
    if request.method == 'POST':
        form = CanvasForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            return HttpResponseRedirect('/canvases/')
    else:
        form = CanvasForm() # blank form

    return render(request, 'app/canvas_form.html', {'form': form[field]})


class CanvasList(ListView):
    model = Canvas


class CanvasDetailView(DetailView):
    model = Canvas


class CanvasCreate(CreateView):
    model = Canvas
    form_class = CanvasForm


class CanvasDelete(DeleteView):
    model = Canvas
    success_url = reverse_lazy('canvas-list')

