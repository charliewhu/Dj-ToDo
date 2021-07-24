from django.urls import path, include
from django.contrib.auth.views import LogoutView
from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name = 'todo'),

    #auth views
    path('login/', views.Login.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),

    #crud views
    path('<int:pk>/', views.TodoDetail.as_view(), name= 'todo_detail'),
    path('create/', views.TodoCreate.as_view(), name = 'todo_create'),
    path('update/<int:pk>/', views.TodoUpdate.as_view(), name = 'todo_update'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name = 'todo_delete'),
]