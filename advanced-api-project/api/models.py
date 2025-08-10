from django.db import models

class Author(models.Model)
    name = CharField


class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.CharField(max_length=255)
# Create your models here.
