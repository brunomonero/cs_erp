# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='Preencha com a Sigla do Cliente.', unique=True, max_length=4, verbose_name='Sigla')),
                ('name', models.CharField(help_text='Preencha com Nome do Cliente.', max_length=256, verbose_name='Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
