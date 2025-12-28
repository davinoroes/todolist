from django import forms
from todolist.models import TaskModel

class TaskForm(forms.ModelForm):
    class meta:
        model = TaskModel
        fields = 'tittle'

    