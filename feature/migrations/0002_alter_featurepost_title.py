# Generated by Django 4.2.6 on 2023-10-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurepost',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
