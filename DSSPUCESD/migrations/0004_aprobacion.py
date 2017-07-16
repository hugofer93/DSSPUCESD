# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSSPUCESD', '0003_auto_20170713_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aprobacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('porcentaje', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Aprobacion',
                'verbose_name_plural': 'Aprobacion',
            },
        ),
    ]
