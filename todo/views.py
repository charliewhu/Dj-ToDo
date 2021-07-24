from typing import ContextManager
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Todo



class TodoList(ListView):
    model               = Todo
    context_object_name = 'todos'


class TodoDetail(DetailView):
    model               = Todo
    context_object_name = 'todo'


class TodoCreate(CreateView):
    model       = Todo
    fields      = '__all__'
    success_url = reverse_lazy('todo')

class TodoUpdate(UpdateView):
    model       = Todo
    fields      = '__all__'
    success_url = reverse_lazy('todo')

class TodoDelete(DeleteView):
    model       = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todo')


# def todo_add(request):
#     if(request.method == 'POST'):
#         title   = request.POST['title']
#         text    = request.POST['text']

#         todo = Todo(title=title, text=text)
#         todo.save()

#         return redirect('/')
#     else:
#         return render(request, 'todo/add.html')


