# Generated by Django 3.0 on 2023-10-01 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]