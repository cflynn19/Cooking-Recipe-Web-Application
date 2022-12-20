from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Search(models.Model):
    image = models.ImageField(upload_to="images/")