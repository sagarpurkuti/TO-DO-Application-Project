from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #it jus redirects uses to cretain page
from .models import Task

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin




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

class TaskList(LoginRequiredMixin, ListView):
    model=Task
    context_object_name='tasks'
    template_name = 'base/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['color']='red'

        # print("all tasks:", Task.objects.all())

        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        # print("tasks for user:", context['tasks'])
        return context
    

class TaskDetail(LoginRequiredMixin, DetailView):
    model=Task
    context_object_name='task'
    template_name='base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = '__all__'  #django already creates model form and we can define it here what to include in form
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasklist') #hyper links to the homepage

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # fields = '__all__'
    fields = ['title','description','complete']
    success_url=reverse_lazy('tasklist')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('tasklist')
    template_name = 'base/task_confirm_delete.html'
