# Generated by Django 4.2.5 on 2023-09-16 05:23

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_enrol_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentjoin',
            name='mobile_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
