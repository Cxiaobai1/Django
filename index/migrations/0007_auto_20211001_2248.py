# Generated by Django 3.2.7 on 2021-10-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_book_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='index.BOOk'),
        ),
    ]