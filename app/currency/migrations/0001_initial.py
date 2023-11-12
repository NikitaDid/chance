# Generated by Django 4.2.7 on 2023-11-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=5)),
                ('type', models.DateTimeField()),
                ('created', models.CharField(max_length=3)),
            ],
        ),
    ]