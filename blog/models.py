from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    def __str__(self):
        return self.content