"""
Definition of models.
"""

from django.db import models

class Person(models.Model):
    Name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')



# Create your models here.
