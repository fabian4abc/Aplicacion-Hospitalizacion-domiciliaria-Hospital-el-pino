# Generated by Django 3.0.7 on 2020-11-23 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita', '0005_visita_observaciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='observaciones',
            field=models.CharField(default=' ', max_length=30000),
        ),
    ]
