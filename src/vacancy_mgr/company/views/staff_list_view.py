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
from company.models import Department, Staff
from company.forms import SearchStaffForm


class StaffListView(FormView):
    """
    スタッフリスト
    """
    form_class = SearchStaffForm
    template_name = 'company/staff_list.html'
    user = None
    all_staffs = False
    staffs = None
    filter_name = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404
        if not self.user.is_company_admin:
            raise Http404

        self.staffs = Staff.objects.order_by(
            'priority',
            'department__priority',
            'department__id'
            'id').all()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['all_staffs'] = self.all_staffs
        if self.all_staffs:
            if self.filter_name:
                context['staffs'] = self.staffs.filter(
                    last_name__icontains=self.filter_name,
                ).all()
            else:
                context['staffs'] = self.staffs
        else:
            if self.filter_name:
                context['staffs'] = self.staffs.filter(
                    is_deleted=False,
                    last_name__icontains=self.filter_name,
                ).all()
            else:
                context['staffs'] = self.staffs.filter(
                    is_deleted=False,
                ).all()

        return context

    def form_valid(self, form):
        if self.request.method in ('POST', 'PUT'):
            if form.data['last_name']:
                self.filter_name = form.data['last_name']

        return self.render_to_response(self.get_context_data())
