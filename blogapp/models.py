from ast import arg
from audioop import reverse
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse 


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title + '   |   ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
       