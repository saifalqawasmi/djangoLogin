from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comments(models.Model):
    title = models.CharField(max_length=255) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name="blogpost_like")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    def numberOfLikes(self):
    	return self.likes.count()