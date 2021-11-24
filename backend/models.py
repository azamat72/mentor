from django.db import models
from django.db.models.fields import TextField
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    full_text = models.TextField()
    date = models.DateTimeField() 
    image = models.ImageField(upload_to='images/', default="img/default-1.png")
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.slug

class Lead(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    full_text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', default="img/default-2.png")
    slug = models.SlugField(max_length=30)


    def __str__(self):
        return self.slug

class Agent(models.Model):
    familiyasi = models.CharField(max_length=50)
    ismi = models.CharField(max_length=50)
    full_text = models.TextField()
    fani = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default="img/default.png")

    def __str__(self):
        return self.familiyasi
