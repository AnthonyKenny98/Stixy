# -*- coding: utf-8 -*-
# @Author: AnthonyKenny98
# @Date:   2020-05-11 21:46:14
# @Last Modified by:   AnthonyKenny98
# @Last Modified time: 2020-05-18 15:23:13

from django.urls import path

from . import views

app_name = 'accounting'
urlpatterns = [

    # Index
    path('', views.index, name='index'),

    # File Upload
    path('upload', views.file_upload, name='upload'),

    # List of Objects
    path('<str:model>', views.table, name='table'),
    path('<str:model>/<int:pk>', views.detail, name='detail')

]
