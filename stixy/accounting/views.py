"""Views for Accounting App."""
# from django.http import HttpResponse
from django.shortcuts import render

from . import models as app_models


def index(request):
    """Index View."""
    context = {}
    return render(request, 'accounting/index.html', context)


def table(request, model):
    """Table View."""
    model_class = getattr(app_models, model)
    context = {
        'meta': model_class,
        'data': model_class.objects.all()
    }
    return render(request, 'accounting/table.html', context)


def list(request, model):
    """List View."""
    # Get Model Class from model param
    model_class = getattr(app_models, model)
    context = {'list': model_class.objects.order_by('name')}
    return render(request, 'accounting/list.html', context)


def detail(request, model, pk):
    """Detail View."""
    # Get Model Class from model param
    model_class = getattr(app_models, model)
    context = {'item': model_class.objects.get(pk=pk)}
    return render(request, 'accounting/detail.html', context)
