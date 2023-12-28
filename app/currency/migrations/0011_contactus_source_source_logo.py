# Generated by Django 4.2.7 on 2023-12-28 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0010_requestresponselog'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currency.source'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='source',
            name='logo',
            field=models.FileField(blank=True, default=None, null=True, upload_to='static/', verbose_name='Logo'),
        ),
    ]
