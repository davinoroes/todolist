from django.shortcuts import render
from django.views.generic import ListView
from todolist.models import TaskModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from todolist.forms import TaskForm
from django.urls import reverse_lazy

# Create your views here.

class TasksView(LoginRequiredMixin,ListView):
    model = TaskModel
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tasks = TaskModel.objects.filter(user=self.request.user)
        search = self.request.GET.get('search')
        if search:
            tasks = tasks.filter(tittle__icontains=search)
        return tasks.order_by('tittle')
    
class CreateTaskView(LoginRequiredMixin,CreateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'newtask.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = TaskModel
    template_name = 'tasksdelete.html'
    success_url = reverse_lazy('task_list')

class UpdateTaskView(LoginRequiredMixin,UpdateView):
    model = TaskModel
    fields = ["tittle"]
    template_name = 'tasksupdate.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    


    
    

