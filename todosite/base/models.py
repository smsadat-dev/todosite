from django.db import models
from django.contrib.auth.models import User


class TodoTaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    taskName = models.CharField(max_length=50, blank=True)
    description = models.TextField(null=True, blank=True)
    isCompleted = models.BooleanField(default=False)
    creationTime = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.taskName
    
    class Meta:
        ordering = []