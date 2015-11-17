# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('status', models.BooleanField(default=True)),
                ('imagen', models.ImageField(null=True, upload_to=b'Productos/', blank=True)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('stock', models.IntegerField()),
                ('categoria', models.ManyToManyField(to='prod.CategoriaProducto', null=True, blank=True)),
            ],
        ),
    ]
