# Generated by Django 3.2.9 on 2021-11-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_articles_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
