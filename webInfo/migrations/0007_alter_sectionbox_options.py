# Generated by Django 4.2.6 on 2023-11-09 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webInfo', '0006_alter_headline_options_alter_headline_headlines'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sectionbox',
            options={'ordering': ['serial'], 'verbose_name': 'Section Box', 'verbose_name_plural': 'Section Boxs'},
        ),
    ]
