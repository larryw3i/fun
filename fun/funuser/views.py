
# Create your views here.

import math
import os

import magic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import (Http404, HttpResponseRedirect, redirect, render,
                              reverse)
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from fun import settings, funvalue
from .models import Funuser, funuser_mame
from .modelforms import FunuserModelForm
from .apps import FunuserConfig

from django.core.files import File
from django.contrib.auth.models import User


funuser_create_template = \
    f'{FunuserConfig.name}/{funuser_mame}{funvalue.create_html}'
funuser_detail_template = \
    f'{FunuserConfig.name}/{funuser_mame}{funvalue.detail_html}'
funuser_delete_template = \
    f'{FunuserConfig.name}/{funuser_mame}{funvalue.delete_html}'
funuser_update_template = \
    f'{FunuserConfig.name}/{funuser_mame}{funvalue.update_html}'
funuser_list_template = \
    f'{FunuserConfig.name}/{funuser_mame}{funvalue.list_html}'


class FunuserUpdateView(LoginRequiredMixin, UpdateView):

    model = Funuser
    form_class = FunuserModelForm
    template_name = funuser_update_template
    success_url = reverse_lazy('funuser:funuser_update')

    def get_object(self, queryset=None):
        default_avatar_file_path = os.path.join(
            settings.SERVE_STATIC_ROOT, 'images', 'x_dove.webp')
            
        is_funuser_created = Funuser.objects.filter(
            user=self.request.user).exists()

        if not is_funuser_created:
            new_funuser = Funuser(\
                user=self.request.user, 
                full_name = self.request.user.username)
            new_funuser.save()

            return new_funuser
        # super().get_object(queryset=queryset)
        funuser = Funuser.objects.get(user=self.request.user)
        funuser.full_name = self.request.user.username
        return funuser

    def form_valid(self, form):

        if not Funuser.objects.filter(
                user=self.request.user, id=form.instance.id).exists():
            form.add_error('full_name',  _('Nice try'))
            return render(
                self.request, funuser_update_template, context={'form': form})
        return super().form_valid(form)


class FunuserDetailView(LoginRequiredMixin, DetailView):

    model = Funuser
    template_name = funuser_detail_template

    def __init__(self):
        self.is_funuser_created = False
        super().__init__()

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
        context_data['is_funuser_created'] = self.is_funuser_created
        return context_data

    def get_object(self, queryset=None):

        self.is_funuser_created = Funuser.objects.filter(
            user__id=self.kwargs['user']).exists()

        if not (self.is_funuser_created):
            return Funuser(user=self.request.user)

        # super().get_object(queryset=queryset)
        return Funuser.objects.get(user__id=self.kwargs['user'])
