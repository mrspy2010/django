# Generated by Django 3.2.9 on 2021-11-13 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211113_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
