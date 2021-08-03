from django.db import models
from django.db.models.deletion import CASCADE

class Author(models.Model):
    author = models.CharField(max_length=100)
    bio = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
