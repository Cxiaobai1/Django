# Generated by Django 3.2.8 on 2021-10-19 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20211015_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extenduserinfo',
            name='user',
        ),
    ]
