from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name = 'todo'),
    path('<int:pk>/', views.TodoDetail.as_view(), name= 'todo_detail'),
    path('add/', views.todo_add, name='todo_add'),
]