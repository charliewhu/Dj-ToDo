from typing import ContextManager
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Todo



class TodoList(ListView):
    model = Todo
    context_object_name = 'todos'


class TodoDetail(DetailView):
    model = Todo
    context_object_name = 'todo'


def todo_add(request):
    if(request.method == 'POST'):
        title   = request.POST['title']
        text    = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/')
    else:
        return render(request, 'todo/add.html')


