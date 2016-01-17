from django.shortcuts import render
from django.views.generic import ListView, DetailView
from app.models import Canvas
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from app.forms import CanvasForm
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory, Textarea, ClearableFileInput
from PIL import Image
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def company(request, pk):
    """
    This is function and not a generic view as it points to a different template from canvas_detail with less fields
    :param request:
    :param pk: primary key of Canvas as a named group of a regular expression at urls
    :return:
    """
    try:
        obj = Canvas.objects.get(pk=pk)
    except Canvas.DoesNotExist:
        raise Http404("Canvas does not exist")
    return render_to_response('app/company_detail.html', {'obj': obj})

@login_required
def update_field(request, pk, field):
    """
    This is function and not a CreateView/Update as it points to a template with less fields
    :param request:
    :param pk: primary key of Canvas
    :param field: which field to update
    :return:
    """
    widgets = {}
    if field=='logo':
        widgets[field] = ClearableFileInput()
    else:
        widgets[field] = Textarea(attrs={'rows':4, 'cols':150})
    CanvasForm = modelform_factory(Canvas, fields=(field,), widgets=widgets)
    if request.method == 'POST':
        form = CanvasForm(request.POST)
        if form.is_valid():
            obj = Canvas.objects.get(id=pk)
            if obj.originalauthor == request.user: # more maintainable than dfunckt/django-rules
                setattr(obj, field, form.cleaned_data[field])
                obj.save()
                return HttpResponseRedirect('/canvas/'+pk)
            else:
                return HttpResponseRedirect('/login/')
    else:
        form = CanvasForm(instance = Canvas.objects.get(id=pk))

    return render(request, 'app/canvas_form.html', {'formfield': form})


def voteup(request, pk):
    """
    This is function and not a CreateView/Update as it points to a template with less fields
    :param request:
    :param pk: primary key of Canvas
    :param field: which field to update
    :return:
    """
    obj = Canvas.objects.get(id=pk)
    if request.user.is_authenticated(): # decorator login_required would redirect
        obj.upvotes = obj.upvotes + 1
        obj.save()
    return HttpResponse(obj.upvotes) # necessary for AJAX


def votedown(request, pk):
    """
    This is function and not a CreateView/Update as it points to a template with less fields
    :param request:
    :param pk: primary key of Canvas
    :param field: which field to update
    :return:
    """
    obj = Canvas.objects.get(id=pk)
    if request.user.is_authenticated(): # decorator login_required would redirect
        obj.downvotes = obj.downvotes + 1
        obj.save()
    return HttpResponse(obj.downvotes)


@login_required
def create_canvas(request):
    """
    This is function and not a CreateView/Update as it points to a template with less fields
    :param request:
    :param pk: primary key of Canvas
    :param field: which field to update
    :return:
    """
    if request.method == 'POST':
        form = CanvasForm(request.POST)
        if form.is_valid():
            form.cleaned_data['originalauthor'] = request.user
            data = ContentFile(request.FILES['logo'].file.read())
            filename = request.FILES['logo'].name
            form.cleaned_data['logo'] = filename
            default_storage.save(filename, data)
            obj = Canvas.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/canvas/%d" % obj.id)
    else:
        form = CanvasForm() # blank form

    return render(request, 'app/canvas_new.html', {'company': form['company'],'description': form['description'],'logo': form['logo']})


class CanvasList(ListView):
    """
    For debugging, check as_view() http://ccbv.co.uk/projects/Django/1.8/django.views.generic.list/ListView/
    """
    model = Canvas


class CanvasDetailView(DetailView):
    model = Canvas


class CanvasDelete(DeleteView):
    model = Canvas
    success_url = reverse_lazy('canvas-list')

