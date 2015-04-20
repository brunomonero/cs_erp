# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Preencha com Nome da Fun\xe7\xe3o.', max_length=256, verbose_name='Fun\xe7\xe3o')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Preencha com Nome da Lista de Pre\xe7o.', max_length=256, verbose_name='Lista de Pre\xe7o')),
                ('price', models.DecimalField(help_text='Preencha com o Pre\xe7o da Fun\xe7\xe3o.', verbose_name='Pre\xe7o', max_digits=5, decimal_places=2)),
                ('contract', models.ForeignKey(verbose_name='Contrato', to='sales.Contract', help_text='Selecione um Contrato.')),
                ('function', models.ForeignKey(verbose_name='Fun\xe7\xe3o', to='sales.Function', help_text='Selecione uma Fun\xe7\xe3o.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
