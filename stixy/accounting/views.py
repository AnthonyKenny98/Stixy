"""Views for Accounting App."""
# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import models as app_models
from .forms import FileUploadForm
from .functions import create_transactions_from_csv


def index(request):
    """Index View."""
    context = {}
    return render(request, 'accounting/index.html', context)

# General Views


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


# Function Specific Views

def file_upload(request):
    """Handle file upload."""
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            create_transactions_from_csv(request.FILES['file'])
            return HttpResponseRedirect(reverse('accounting:index'))
    else:
        form = FileUploadForm()
    return render(request, 'accounting/form.html', {'form': form})
