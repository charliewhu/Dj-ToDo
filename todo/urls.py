from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name = 'todo'),
    path('<int:pk>/', views.TodoDetail.as_view(), name= 'todo_detail'),
    path('create/', views.TodoCreate.as_view(), name='todo_create'),
    path('update/<int:pk>/', views.TodoUpdate.as_view(), name= 'todo_update'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name= 'todo_delete'),
]