# Generated by Django 3.0 on 2023-10-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0005_problem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='email',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
