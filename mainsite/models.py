from django.db import models

# Create your models here.
class Home(models.Model):
    banner = models.ImageField(upload_to='uploads/')
    content = models.TextField()
    publish = models.BooleanField()

class About(models.Model):
    banner = models.ImageField(upload_to='uploads/')
    content = models.TextField()
    publish = models.BooleanField()