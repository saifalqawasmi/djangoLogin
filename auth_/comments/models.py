from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comments(models.Model):
    title = models.CharField(max_length=255) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    content = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title