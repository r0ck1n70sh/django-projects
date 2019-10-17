import datetime

from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title= models.CharField(max_length=150)
    body= models.TextField()
    timestamp= models.DateTimeField(default=timezone.now())
   
    def __str__(self):
        return self.title
