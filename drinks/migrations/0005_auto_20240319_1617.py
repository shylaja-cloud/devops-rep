# Generated by Django 3.2.25 on 2024-03-19 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_drink_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='drink',
            name='ingredients',
            field=models.TextField(default=''),
        ),
    ]