# Generated by Django 3.1.2 on 2020-10-20 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprogress', '0007_auto_20201020_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledcourse',
            name='course',
            field=models.ManyToManyField(to='userprogress.Course'),
        ),
    ]
