# Generated by Django 4.0.6 on 2022-07-27 03:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0002_integrantes_delete_integrante_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='data_creation_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 7, 27, 0, 19, 18, 883518)),
        ),
    ]
