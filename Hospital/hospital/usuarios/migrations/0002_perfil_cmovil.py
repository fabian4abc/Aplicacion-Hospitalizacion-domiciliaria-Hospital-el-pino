# Generated by Django 3.0.7 on 2020-11-03 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cmovil',
            field=models.CharField(default='12345', max_length=20),
        ),
    ]