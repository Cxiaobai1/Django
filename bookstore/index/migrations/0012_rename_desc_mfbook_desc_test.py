# Generated by Django 3.2.7 on 2021-10-14 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20211014_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mfbook',
            old_name='desc',
            new_name='desc_test',
        ),
    ]
