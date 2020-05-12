
# from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import AccountClass, AccountGroup

import sys



def index(request):
    context = {}
    return render(request, 'accounting/index.html', context)

def list(request, model):

    # Get Model Class from model param
    Model = getattr(sys.modules[__name__], model)
    context = {'list': Model.objects.order_by('name')}
    return render(request, 'accounting/list.html', context)

def detail(request, model, pk):

    # Get Model Class from model param
    Model = getattr(sys.modules[__name__], model)
    context = {'item': Model.objects.get(pk=pk)}
    return render(request, 'accounting/detail.html', context)