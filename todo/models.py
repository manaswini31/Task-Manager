from django.db import models
from django.utils import timezone

class Item(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
