from django.db import models

# Create your models here.
# Adapted from minimal example https://github.com/axelpale/minimal-django-file-upload-example/
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
