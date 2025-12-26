from django.shortcuts import render
from django.views.generic import ListView
from todolist.models import TaskModel
from django.contrib.auth.mixins import LoginRequiredMixin

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

    
    

