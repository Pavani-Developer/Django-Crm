# Generated by Django 4.2.5 on 2023-09-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_studentjoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=40)),
                ('trainername', models.CharField(max_length=40)),
                ('date', models.CharField(max_length=40)),
                ('time', models.CharField(max_length=40)),
                ('coursetype', models.CharField(max_length=40)),
            ],
        ),
    ]