from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)


