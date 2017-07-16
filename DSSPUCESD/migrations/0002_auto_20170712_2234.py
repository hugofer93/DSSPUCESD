# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DSSPUCESD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParamPrimario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('porcentaje', models.DecimalField(max_digits=4, decimal_places=2)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'parametro',
                'verbose_name_plural': 'parametros',
            },
        ),
        migrations.CreateModel(
            name='ParamSecundario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('porcentaje', models.DecimalField(max_digits=4, decimal_places=2)),
                ('param_primario', models.ForeignKey(to='DSSPUCESD.ParamPrimario')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'parametro secundario',
                'verbose_name_plural': 'parametros secundarios',
            },
        ),
        migrations.CreateModel(
            name='ParamTerciario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('porcentaje', models.DecimalField(max_digits=4, decimal_places=2)),
                ('param_secundario', models.ForeignKey(to='DSSPUCESD.ParamSecundario')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'parametro secundario',
                'verbose_name_plural': 'parametros secundarios',
            },
        ),
        migrations.RemoveField(
            model_name='merito',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='oposicion',
            name='persona',
        ),
        migrations.RemoveField(
            model_name='parametro',
            name='merito',
        ),
        migrations.RemoveField(
            model_name='parametro',
            name='oposicion',
        ),
        migrations.RemoveField(
            model_name='paramprincipalmerito',
            name='merito',
        ),
        migrations.RemoveField(
            model_name='paramprincipaloposicion',
            name='oposicion',
        ),
        migrations.RemoveField(
            model_name='paramsecundariomerito',
            name='paramprincipal',
        ),
        migrations.RemoveField(
            model_name='paramsecundariooposicion',
            name='paramprincipal',
        ),
        migrations.DeleteModel(
            name='Merito',
        ),
        migrations.DeleteModel(
            name='Oposicion',
        ),
        migrations.DeleteModel(
            name='Parametro',
        ),
        migrations.DeleteModel(
            name='ParamPrincipalMerito',
        ),
        migrations.DeleteModel(
            name='ParamPrincipalOposicion',
        ),
        migrations.DeleteModel(
            name='ParamSecundarioMerito',
        ),
        migrations.DeleteModel(
            name='ParamSecundarioOposicion',
        ),
    ]
