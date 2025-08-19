from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class post(models.Model):
    title: models.CharField(max_length=200)
    content: models.TextField()
    published_date: models.DateTimeField(auto_now_add=True)

# Create your models here.
