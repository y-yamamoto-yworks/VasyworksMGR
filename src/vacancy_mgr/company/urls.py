"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
from django.urls import include, path
from django.views.generic import TemplateView
from company.views import *

urlpatterns = [
    path('department_list/', DepartmentListView.as_view(), name='company_department_list'),
    path('department_list/all/', DepartmentListView.as_view(all_departments=True), name='company_all_department_list'),
    path('department/<str:idb64>', DepartmentView.as_view(), name='company_department'),
    path('create_department/', CreateDepartmentView.as_view(), name='company_create_department'),
    path('staff_list/', StaffListView.as_view(), name='company_staff_list'),
    path('staff_list/all/', StaffListView.as_view(all_staffs=True), name='company_all_staff_list'),
    path('staff/<str:idb64>', StaffView.as_view(), name='company_staff'),
    path('create_staff/', CreateStaffView.as_view(), name='company_create_staff'),
    path('create_staff/<str:department_idb64>', CreateStaffView.as_view(), name='company_create_staff'),

    path('', CompanyView.as_view(), name='company_index'),
]
