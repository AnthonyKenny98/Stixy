"""Views for Accounting App."""
# from django.http import HttpResponse
from django.shortcuts import render

from .models import AccountClass, AccountGroup, \
    Account, SubAccount, BankAccount, Transaction, Entry  # noqa: F401

import sys


def index(request):
    """Index View."""
    context = {}
    return render(request, 'accounting/index.html', context)


def table(request, model):
    """Table View."""
    Model = getattr(sys.modules[__name__], model)  # noqa: N806
    context = {
        'meta': Model,
        'data': Model.objects.all()
    }
    return render(request, 'accounting/table.html', context)


def list(request, model):
    """List View."""
    # Get Model Class from model param
    Model = getattr(sys.modules[__name__], model)  # noqa: N806
    context = {'list': Model.objects.order_by('name')}
    return render(request, 'accounting/list.html', context)


def detail(request, model, pk):
    """Detail View."""
    # Get Model Class from model param
    Model = getattr(sys.modules[__name__], model)  # noqa: N806
    context = {'item': Model.objects.get(pk=pk)}
    return render(request, 'accounting/detail.html', context)
