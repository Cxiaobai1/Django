# Generated by Django 3.2.7 on 2021-10-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_mfbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfbook',
            name='author',
            field=models.CharField(max_length=24, null=True, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='mfbook',
            name='desc',
            field=models.CharField(default='无描述', max_length=255, null=True, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='mfbook',
            name='img_ul',
            field=models.CharField(default='无路径', max_length=255, null=True, verbose_name='图片路径'),
        ),
    ]
