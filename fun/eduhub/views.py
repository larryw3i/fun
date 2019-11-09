
from django.shortcuts import render
from .modelforms import LabelModelForm
from .apps import EduhubConfig
from .models import Label
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from django.shortcuts import render, reverse, redirect

# Create your views here.


class LabelCreateView( CreateView, LoginRequiredMixin ):
    model = Label
    template_name = f'{EduhubConfig.name}/label_create.html'
    fields = ['name', 'cover', 'comment']

    def post(self, request, *args, **kwargs):
        label = Label(request.POST, request.FILES)
        label.author = request.user
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('label_list') # super().get_success_url()
