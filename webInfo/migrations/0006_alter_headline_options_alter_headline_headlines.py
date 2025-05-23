# Generated by Django 4.2.6 on 2023-11-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_is_highlight_on_section'),
        ('webInfo', '0005_headnews_delete_headlinenews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headline',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Head line', 'verbose_name_plural': 'Head lines'},
        ),
        migrations.AlterField(
            model_name='headline',
            name='headlines',
            field=models.ManyToManyField(blank=True, to='news.post', verbose_name='Head lines'),
        ),
    ]
