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
    path('management_info_list/', ManagementInfoListView.as_view(), name='info_management_info_list'),
    path('edit_management_info/<str:idb64>', EditManagementInfoView.as_view(), name='info_edit_management_info'),
    path('create_management_info/', CreateManagementInfoView.as_view(), name='info_create_management_info'),
    path('delete_management_info/<str:idb64>', DeleteManagementInfoView.as_view(), name='info_delete_management_info'),

    path('', TemplateView.as_view(template_name='404.html'), name='info_index'),
]
