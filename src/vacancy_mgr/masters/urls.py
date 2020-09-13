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
    path('guarantee_company_list/', GuaranteeCompanyListView.as_view(), name='masters_guarantee_company_list'),
    path('guarantee_company/<str:idb64>', GuaranteeCompanyView.as_view(), name='masters_guarantee_company'),
    path('create_guarantee_company/', CreateGuaranteeCompanyView.as_view(), name='masters_create_guarantee_company'),

    path('insurance_company_list/', InsuranceCompanyListView.as_view(), name='masters_insurance_company_list'),
    path('insurance_company/<str:idb64>', InsuranceCompanyView.as_view(), name='masters_insurance_company'),
    path('create_insurance_company/', CreateInsuranceCompanyView.as_view(), name='masters_create_insurance_company'),

    path('', TemplateView.as_view(template_name='404.html'), name='masters_index'),
]
