from typing import ContextManager
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo

# Create your views here.

def todo(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos,
    }
    return render(request, 'todo/index.html', context)


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    context = {
        'todo':todo,
    }
    return render(request, 'todo/detail.html', context)

def todo_add(request):
    if(request.method == 'POST'):
        title   = request.POST['title']
        text    = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/')
    else:
        return render(request, 'todo/add.html')