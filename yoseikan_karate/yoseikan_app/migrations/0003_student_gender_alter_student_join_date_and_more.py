# Generated by Django 4.1.3 on 2022-11-15 06:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('yoseikan_app', '0002_student_address_student_join_date_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='join_date',
            field=models.CharField(default='15/11/2022', max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
