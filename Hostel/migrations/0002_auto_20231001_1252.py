# Generated by Django 3.0 on 2023-10-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenants',
            name='room_no',
            field=models.CharField(max_length=10),
        ),
    ]