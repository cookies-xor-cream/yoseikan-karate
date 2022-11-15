from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.CharField(max_length=128)
    validated = models.BooleanField()
