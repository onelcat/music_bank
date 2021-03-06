# Generated by Django 3.1.6 on 2021-02-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0005_auto_20210216_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='open_time',
            field=models.DateTimeField(auto_now=True, verbose_name='time opened'),
        ),
        migrations.AlterField(
            model_name='file',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='time published'),
        ),
    ]
