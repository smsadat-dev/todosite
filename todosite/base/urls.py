from django.urls import path, include
from django.shortcuts import render, redirect

from . import views

app_name = 'base'

urlpatterns = [
    path('tasks/', views.TodoListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task'),

    path('create/', views.CreateTaskView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateTaskView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete'),

    path('', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register/', views.RegisterPageView.as_view(), name='register')
]
