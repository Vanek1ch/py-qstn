from django.db import models

# Create your models here.
class Person(models.Model):
    login = models.CharField(max_length=9)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    number = models.IntegerField()
    EI = models.CharField(max_length=20)
    date = models.DateField()