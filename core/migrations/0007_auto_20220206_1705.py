# Generated by Django 2.1.7 on 2022-02-06 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220206_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 2, 6, 17, 5, 52, 862795)),
        ),
    ]
