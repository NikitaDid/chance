# Generated by Django 4.2.7 on 2023-11-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rate_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rate',
            name='type',
            field=models.CharField(max_length=3),
        ),
    ]