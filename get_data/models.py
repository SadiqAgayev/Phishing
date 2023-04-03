from django.db import models

# Create your models here.
class Info(models.Model):
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)