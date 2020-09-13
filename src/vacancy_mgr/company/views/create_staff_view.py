"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
from abc import ABCMeta, abstractmethod
from django.conf import settings
from django.db import transaction
from django.db.models import Q
from django.utils import timezone
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text, escape_uri_path
from django.utils.translation import gettext_lazy as _
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, FormView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from dateutil.relativedelta import relativedelta
from PIL import Image
from lib.convert import *
from lib.functions import *
from company.forms import CreateStaffForm
from company.models import Company, Department, Staff


class CreateStaffView(FormView):
    """
    スタッフ作成
    """
    form_class = CreateStaffForm
    template_name = 'company/create_staff.html'
    success_url = reverse_lazy('company_staff_list')
    user = None
    department = None
    staff = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404
        if not self.user.is_company_admin:
            raise Http404

        department_idb64 = kwargs.get('department_idb64')
        if department_idb64:
            department_id = 0
            try:
                idb64 = force_text(urlsafe_base64_decode(department_idb64))
                if idb64.isdecimal():
                    department_id = xint(idb64)
            except ValueError:
                department_id = 0

            if department_id != 0:
                self.department = Department.objects.get(pk=department_id)

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.staff:
            url = reverse_lazy('company_staff', kwargs={'idb64': self.staff.idb64})
            back_url = xstr(reverse_lazy('company_staff_list'))
            url += '?back_url=' + back_url

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['department'] = self.department
        context['staff'] = self.staff
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため追加できません。')
        elif self.request.method == 'POST':
            first_name = self.request.POST['first_name']
            last_name = self.request.POST['last_name']

            data = Staff()
            data.first_name = first_name
            data.last_name = last_name
            data.priority = 100
            data.is_pm_staff = True
            data.is_publish_vacancy = True
            data.created_at = timezone.datetime.now()
            data.is_stopped = False
            data.is_deleted = False

            if self.department:
                data.department = self.department

            data.save()
            self.staff = data
            messages.success(self.request, '追加しました。')

        return super().form_valid(form)
