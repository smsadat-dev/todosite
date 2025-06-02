from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import TodoTaskModel


class TodoListView( ListView):
    model = TodoTaskModel
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(isCompleted=False).count()

        search_input = self.request.GET.get('searchbar') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(taskName__istartswith=search_input)
        
        context['search_input'] = search_input

        return context
        
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = TodoTaskModel
    context_object_name = 'task'

class CreateTaskView(LoginRequiredMixin, CreateView):
    model = TodoTaskModel
    fields = ['taskName', 'description', 'isCompleted']
    success_url = reverse_lazy('base:tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = TodoTaskModel
    fields = ['taskName', 'description', 'isCompleted']
    success_url = reverse_lazy('base:tasks')

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = TodoTaskModel
    fields = '__all__'
    context_object_name = 'task'
    success_url = reverse_lazy('base:tasks')


# Auth view functions


class LoginPageView(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('base:tasks')
    
class RegisterPageView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('base:tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)
        