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
    path('trader_list/', TraderListView.as_view(), name='trader_trader_list'),
    path('trader_list/all/', TraderListView.as_view(all_traders=True), name='trader_all_trader_list'),
    path('detail/<str:idb64>', TraderView.as_view(), name='trader_detail'),
    path('create_trader/', CreateTraderView.as_view(), name='trader_create_trader'),

    path('trader_group_list/', TraderGroupListView.as_view(), name='trader_trader_group_list'),
    path('trader_group_list/all/', TraderGroupListView.as_view(all_trader_groups=True), name='trader_all_trader_group_list'),
    path('trader_group/<str:idb64>', TraderGroupView.as_view(), name='trader_trader_group'),
    path('create_trader_group/', CreateTraderGroupView.as_view(), name='trader_create_trader_group'),

    path('', TemplateView.as_view(template_name='404.html'), name='trader_index'),
]
