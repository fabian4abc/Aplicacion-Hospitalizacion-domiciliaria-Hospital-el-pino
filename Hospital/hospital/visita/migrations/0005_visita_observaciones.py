# Generated by Django 3.0.7 on 2020-11-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita', '0004_remove_visita_nombre2'),
    ]

    operations = [
        migrations.AddField(
            model_name='visita',
            name='observaciones',
            field=models.CharField(default=' ', max_length=30000),
        ),
    ]
