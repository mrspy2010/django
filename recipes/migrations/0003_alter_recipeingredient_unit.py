# Generated by Django 3.2.9 on 2021-11-15 15:56

from django.db import migrations, models
import recipes.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20211115_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=50, validators=[recipes.validators.validate_unit_of_measure]),
        ),
    ]
