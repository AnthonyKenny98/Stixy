# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-05-11 21:46:14
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-05-12 11:01:57

from django.urls import path

from . import views

app_name = 'accounting'
urlpatterns = [

    # Index
    path('', views.index, name='index'),

    # Account Classes
    path(
        'account_class', views.AccountClassList.as_view(),
        name='account_class'),
    path(
        'account_class/<int:pk>', views.AccountClassDetail.as_view(),
        name='account_class'),

    # Account Groups
    path(
        'account_group', views.AccountGroupList.as_view(),
        name='account_group'),
    path(
        'account_group/<int:pk>', views.AccountGroupDetail.as_view(),
        name='account_group')
]
