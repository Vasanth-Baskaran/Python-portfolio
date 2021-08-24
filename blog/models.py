from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()