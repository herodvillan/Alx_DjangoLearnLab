from django.db import models

class post(models.Model):
    title: models.CharField(max_length=200)
    content: models.TextField()
    published_date: models.DateTimeField(auto_now_add=True)

# Create your models here.
