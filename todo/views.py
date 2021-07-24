from typing import ContextManager
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Todo


class Login(LoginView):
    #template_name = 'registration/login.html'
    fields                      = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo')

class Register(FormView):
    form_class                  = UserCreationForm
    template_name               = 'registration/register.html'
    redirect_authenticated_user = True
    success_url                 = reverse_lazy('todo')

    def form_valid(self, form) :
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo')
        return super(Register, self).get()


class TodoList(LoginRequiredMixin, ListView):
    model               = Todo
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(user=self.request.user)
        context['count'] = context['todos'].filter(complete=False).count()
        return context


class TodoDetail(LoginRequiredMixin, DetailView):
    model               = Todo
    context_object_name = 'todo'


class TodoCreate(LoginRequiredMixin, CreateView):
    model       = Todo
    fields      = ['title', 'text',]
    success_url = reverse_lazy('todo')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreate, self).form_valid(form)


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model       = Todo
    fields      = ['title', 'text', 'complete']
    success_url = reverse_lazy('todo')


class TodoDelete(LoginRequiredMixin, DeleteView):
    model               = Todo
    context_object_name = 'todo'
    success_url         = reverse_lazy('todo')




