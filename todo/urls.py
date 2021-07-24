from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.todo, name = 'todo'),
    path('<int:pk>/', views.todo_detail, name= 'todo_detail'),
    path('add/', views.todo_add, name='todo_add'),
]