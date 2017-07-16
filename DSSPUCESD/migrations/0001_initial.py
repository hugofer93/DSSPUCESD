# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Merito',
                'verbose_name': 'Merito',
            },
        ),
        migrations.CreateModel(
            name='Oposicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Oposiciones',
                'verbose_name': 'Oposicion',
            },
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('aceptacion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('merito', models.OneToOneField(to='DSSPUCESD.Merito')),
                ('oposicion', models.OneToOneField(to='DSSPUCESD.Oposicion')),
            ],
            options={
                'verbose_name_plural': 'Parametros',
                'verbose_name': 'Parametro',
            },
        ),
        migrations.CreateModel(
            name='ParamPrincipalMerito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
                ('merito', models.ForeignKey(to='DSSPUCESD.Merito')),
            ],
            options={
                'verbose_name_plural': 'Parametros Principales Merito',
                'verbose_name': 'Parametro Principal Merito',
            },
        ),
        migrations.CreateModel(
            name='ParamPrincipalOposicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
                ('oposicion', models.ForeignKey(to='DSSPUCESD.Oposicion')),
            ],
            options={
                'verbose_name_plural': 'Parametros Principales Oposicion',
                'verbose_name': 'Parametro Principal Oposicion',
            },
        ),
        migrations.CreateModel(
            name='ParamSecundarioMerito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
                ('paramprincipal', models.ForeignKey(to='DSSPUCESD.ParamPrincipalMerito')),
            ],
            options={
                'verbose_name_plural': 'Parametros Secundarios Merito',
                'verbose_name': 'Parametro Secundario Merito',
            },
        ),
        migrations.CreateModel(
            name='ParamSecundarioOposicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
                ('paramprincipal', models.ForeignKey(to='DSSPUCESD.ParamPrincipalOposicion')),
            ],
            options={
                'verbose_name_plural': 'Parametros Secundarios Oposicion',
                'verbose_name': 'Parametro Secundario Oposicion',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('cedula', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=80)),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Personas',
                'ordering': ['nombre', 'apellido'],
                'verbose_name': 'persona',
            },
        ),
        migrations.AddField(
            model_name='oposicion',
            name='persona',
            field=models.OneToOneField(blank=True, to='DSSPUCESD.Persona', null=True),
        ),
        migrations.AddField(
            model_name='merito',
            name='persona',
            field=models.OneToOneField(blank=True, to='DSSPUCESD.Persona', null=True),
        ),
    ]
