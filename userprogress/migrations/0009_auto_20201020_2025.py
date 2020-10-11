# Generated by Django 3.1.2 on 2020-10-20 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprogress', '0008_auto_20201020_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolledcourse',
            name='course',
        ),
        migrations.AddField(
            model_name='enrolledcourse',
            name='course',
            field=models.ForeignKey(default='Choose Course', on_delete=django.db.models.deletion.CASCADE, related_name='course', to='userprogress.course'),
            preserve_default=False,
        ),
    ]
