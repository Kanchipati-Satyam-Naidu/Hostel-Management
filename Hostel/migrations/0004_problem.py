# Generated by Django 3.0 on 2023-10-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel', '0003_auto_20231001_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('room_no', models.CharField(max_length=10)),
                ('issue', models.CharField(max_length=200)),
            ],
        ),
    ]
