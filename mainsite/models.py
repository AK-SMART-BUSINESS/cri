from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Home(models.Model):
    banner = models.ImageField(upload_to='uploads/')
    content = RichTextUploadingField()
    publish = models.BooleanField()

class About(models.Model):
    banner = models.ImageField(upload_to='uploads/')
    content = RichTextUploadingField()
    publish = models.BooleanField()