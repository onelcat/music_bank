# Generated by Django 3.1.6 on 2021-02-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bee', '0006_auto_20210216_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_path',
            field=models.FileField(upload_to='./upload/file'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(default='none', max_length=16),
        ),
        migrations.AlterField(
            model_name='file',
            name='link_path',
            field=models.FileField(null=True, upload_to='./upload/link'),
        ),
    ]
