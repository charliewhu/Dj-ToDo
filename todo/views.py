from typing import ContextManager
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo


class Login(LoginView):
    template_name = 'registration/login.html'
    fields                      = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo')


class TodoList(LoginRequiredMixin, ListView):
    model               = Todo
    context_object_name = 'todos'


class TodoDetail(LoginRequiredMixin, DetailView):
    model               = Todo
    context_object_name = 'todo'


class TodoCreate(LoginRequiredMixin, CreateView):
    model       = Todo
    fields      = '__all__'
    success_url = reverse_lazy('todo')

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model       = Todo
    fields      = '__all__'
    success_url = reverse_lazy('todo')

class TodoDelete(LoginRequiredMixin, DeleteView):
    model               = Todo
    context_object_name = 'todo'
    success_url         = reverse_lazy('todo')




