"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('owner_list/', OwnerListView.as_view(), name='owner_owner_list'),
    path('owner_list/all/', OwnerListView.as_view(all_owners=True), name='owner_all_owner_list'),
    path('detail/<str:idb64>', OwnerView.as_view(), name='owner_detail'),
    path('create_owner/', CreateOwnerView.as_view(), name='owner_create_owner'),

    path('', TemplateView.as_view(template_name='404.html'), name='owner_index'),
]
