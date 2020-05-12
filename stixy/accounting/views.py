
# from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import AccountClass, AccountGroup


def index(request):
    context = {}
    return render(request, 'accounting/index.html', context)


class AccountClassList(generic.ListView):
    context_object_name = 'list'

    def get_queryset(self):
        return AccountClass.objects.order_by('name')


class AccountClassDetail(generic.DetailView):
    model = AccountClass
    context_object_name = 'item'


class AccountGroupList(generic.ListView):
    context_object_name = 'list'

    def get_queryset(self):
        return AccountGroup.objects.order_by('name')


class AccountGroupDetail(generic.DetailView):
    model = AccountGroup
    context_object_name = 'item'
