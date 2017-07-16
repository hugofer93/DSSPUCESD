# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSSPUCESD', '0002_auto_20170712_2234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paramprimario',
            options={'verbose_name_plural': 'parametros primarios', 'ordering': ['id'], 'verbose_name': 'parametro primario'},
        ),
        migrations.AlterModelOptions(
            name='paramterciario',
            options={'verbose_name_plural': 'parametros terciarios', 'ordering': ['id'], 'verbose_name': 'parametro terciario'},
        ),
    ]
