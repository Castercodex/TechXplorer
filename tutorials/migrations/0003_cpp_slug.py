# Generated by Django 3.1.2 on 2020-10-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0002_auto_20201017_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpp',
            name='slug',
            field=models.SlugField(default='tutorial-1'),
            preserve_default=False,
        ),
    ]