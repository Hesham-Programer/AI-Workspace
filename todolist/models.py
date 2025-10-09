from django.db import models
from django.utils import timezone

# Create your models here.
class TodoList(models.Model):
    todo = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo
