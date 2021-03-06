# Generated by Django 3.0.5 on 2020-08-17 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Новина', 'verbose_name_plural': 'Новини'},
        ),
        migrations.AlterField(
            model_name='post',
            name='fdesc',
            field=models.TextField(max_length=500, verbose_name='Коротке описання'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='static/img/posts/', verbose_name='Зображення: '),
        ),
        migrations.AlterField(
            model_name='post',
            name='sdesc',
            field=models.TextField(verbose_name='Повний опис'),
        ),
    ]
