from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #it jus redirects uses to cretain page
from .models import Task

from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasklist')
    
class CustomLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')

# def tasklist(request):
#     return HttpResponse("hello world")

class TaskList(ListView):
    model=Task
    context_object_name='tasks'

class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
    template_name='base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'  #django already creates model form and we can define it here what to include in form
    success_url = reverse_lazy('tasklist') #hyper links to the homepage

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url=reverse_lazy('tasklist')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('tasklist')
    template_name = 'base/task_confirm_delete.html'
