# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-05-11 21:46:14
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-05-12 13:48:39

from django.urls import path

from . import views

app_name = 'accounting'
urlpatterns = [

    # Index
    path('', views.index, name='index'),

    # List of Objects
    path('<str:model>', views.list, name='list'),
    path('<str:model>/<int:pk>', views.detail, name='detail')

]
