from django.contrib import admin
from todolist.models import TaskModel

# Register your models here.

class TaskAdminModel(admin.ModelAdmin):
    list_display = ('tittle','active','user',)


admin.site.register(TaskModel,TaskAdminModel)