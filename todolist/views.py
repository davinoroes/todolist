from django.shortcuts import render
from django.views.generic import ListView
from todolist.models import TaskModel

# Create your views here.

class TasksView(ListView):
    model = TaskModel
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tasks = super().get_queryset().order_by('tittle')
        search = self.request.GET.get('search')
        if search:
            tasks = tasks.filter(tittle__icontains=search)
        return tasks

    
    

