"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import datetime
import uuid
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
from lib.image_helper import ImageHelper
from lib.media_helper import MediaHelper
from documents.forms import UploadDocumentFileForm
from documents.models import DocumentFile


class UploadDocumentFileView(FormView):
    """
    書類ファイルアップロード
    """
    form_class = UploadDocumentFileForm
    template_name = 'documents/upload_document_file.html'
    success_url = reverse_lazy('menu_index')

    def __init__(self, **kwargs):
        self.user = None
        self.document_file = None
        self.back_url = None

        super().__init__(**kwargs)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = self.request.user
        if not self.user:
            raise Http404

        self.back_url = request.GET.get('back_url')

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = super().get_success_url()
        if self.document_file:
            if self.back_url:
                url = self.back_url
            else:
                url = reverse_lazy('documents_index')
        elif settings.DEMO:
            url = reverse_lazy('documents_index')

        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        if self.back_url:
            context['back_url'] = self.back_url
            context['escaped_back_url'] = escape_uri_path(self.back_url)
        return context

    def form_valid(self, form):
        if settings.DEMO:
            messages.error(self.request, 'DEMOモードのため追加できません。')
        elif self.request.method == 'POST':
            file_title = self.request.POST['file_title']

            file_name = None
            if self.request.FILES['file']:
                file_name = MediaHelper.get_uuid_filename(self.request.FILES['file'].name)
                file_path = MediaHelper.get_upload_document_path(file_name)
                MediaHelper.upload_binary_file(self.request.FILES['file'], file_path)

            if file_title and file_name:
                data = DocumentFile()
                data.file_title = file_title
                data.file_name = file_name
                data.cache_name = MediaHelper.get_uuid_filename(file_name)

                data.created_at = timezone.datetime.now()
                data.created_user = self.user
                data.updated_at = timezone.datetime.now()
                data.updated_user = self.user

                data.save()
                self.document_file = data
                messages.success(self.request, '追加しました。')
            else:
                raise ValueError

        return super().form_valid(form)
