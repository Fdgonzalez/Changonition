from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    face = models.CharField(max_length=500000)