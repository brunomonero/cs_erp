# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Preencha com Nome do Contrato.', max_length=256, verbose_name='Nome')),
                ('initial_date', models.DateField(help_text='Selecione uma data de in\xedcio de vig\xeancia do Contrato.', verbose_name='Data de In\xedcio', auto_now_add=True)),
                ('finish_date', models.DateField(help_text='Selecione uma data de t\xe9rmino de vig\xeancia do Contrato.', verbose_name='Data de T\xe9rmino', auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, to='crm.Customer', help_text='Selecione um Cliente.', null=True, verbose_name='Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
