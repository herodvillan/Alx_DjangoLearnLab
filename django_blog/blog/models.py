from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
# Create your models here.

class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.Date
TimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    posts = models.ManyToManyField(Post)







# # blog/models.py
#
# from django.db import models
# from django.contrib.auth.models import User
# from taggit.managers import TaggableManager # <-- Make sure this import is here
#
# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField()
#     # ... other fields ...
#
#     tags = TaggableManager() # <-- Make sure this line is added to your model
#
#     def __str__(self):
#         return self.title
#
# # If not already implemented, create a Tag model in your blog app that includes a name field.
# # Establish a many-to-many relationship between Tag and Post models to allow assigning multiple tags to a single post and associating multiple posts with a single tag.
# # Use Django’s migrations to create and update the database schema.
