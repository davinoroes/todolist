from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskModel(models.Model):
    tittle = models.CharField(max_length=40, blank=True,null=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.tittle
    




