"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from django.views.generic import TemplateView
from search.views import *

urlpatterns = [
    path('buildings/all/', AllBuildingListView.as_view(), name='search_buildings_all'),
    path('buildings/all/<int:page_number>', AllBuildingListView.as_view(), name='search_buildings_all'),
    path('buildings/area/', AreaBuildingListView.as_view(), name='search_buildings_area'),

    path('', TemplateView.as_view(template_name='404.html'), name='search_index'),
]
