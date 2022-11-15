from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=512)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    join_date = models.CharField(max_length=128)
    validated = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.student_id})'
