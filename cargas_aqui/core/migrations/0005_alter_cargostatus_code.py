# Generated by Django 4.0.4 on 2022-05-05 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cargostatus_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargostatus',
            name='code',
            field=models.CharField(max_length=30, unique=True, verbose_name='Code'),
        ),
    ]
