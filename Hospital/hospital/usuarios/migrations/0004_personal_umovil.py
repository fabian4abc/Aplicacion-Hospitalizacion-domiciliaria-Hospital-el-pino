# Generated by Django 3.0.7 on 2020-11-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_perfil_umovil'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='umovil',
            field=models.CharField(default='Homero', max_length=20),
        ),
    ]