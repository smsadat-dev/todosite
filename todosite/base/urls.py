from django.urls import path, include
from django.shortcuts import render, redirect

from . import viewstasks , viewslogin

app_name = 'base'

urlpatterns = [
    path('tasks/', viewstasks.TodoListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', viewstasks.TaskDetailView.as_view(), name='task'),

    path('create/', viewstasks.CreateTaskView.as_view(), name='create'),
    path('update/<int:pk>/', viewstasks.UpdateTaskView.as_view(), name='update'),
    path('delete/<int:pk>/', viewstasks.DeleteTaskView.as_view(), name='delete'),

    # path('', viewslogin.LoginPageView.as_view(), name='login'),
    # path('logout/', viewslogin.LogoutView.as_view(next_page='base:login'), name='logout'),
    # path('register/', viewslogin.RegisterPageView.as_view(), name='register')
]
