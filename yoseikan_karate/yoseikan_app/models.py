from datetime import datetime
import uuid
from django.db import models

class Student(models.Model):
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    student_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    join_date = models.CharField(max_length=128, default=datetime.today().strftime('%d/%m/%Y'))
    validated = models.BooleanField()
    gender = models.CharField(max_length=32, choices=GENDERS)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.student_id})'
