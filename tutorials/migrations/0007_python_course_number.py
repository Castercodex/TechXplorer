# Generated by Django 3.1.2 on 2020-12-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_auto_20201227_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='python',
            name='course_number',
            field=models.IntegerField(default=1),
        ),
    ]
