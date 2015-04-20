# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='Preencha com a Sigla do Cliente.', unique=True, max_length=4, verbose_name='Sigla')),
                ('name', models.CharField(help_text='Preencha com Nome do Cliente.', max_length=256, verbose_name='Nome')),
                ('type', models.CharField(help_text='Selecione um tipo.', max_length=2, verbose_name='Tipo', choices=[(b'HM', b'Horas e Materiais'), (b'EF', b'Escopo Fechado')])),
                ('status', models.CharField(default=b'AB', help_text='Selecione um Status.', max_length=2, verbose_name='Status', choices=[(b'AB', b'Aberto'), (b'EP', b'Em progresso'), (b'CO', 'Conclu\xeddo'), (b'CA', b'Cancelado')])),
                ('customer', models.ForeignKey(verbose_name='Cliente', to='crm.Customer', help_text='Selecione um Cliente.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('code', models.AutoField(help_text='C\xf6digo da Atividade.', serialize=False, verbose_name='C\xf3digo', primary_key=True)),
                ('name', models.CharField(help_text='Preencha com Nome do Atividade.', max_length=256, verbose_name='Nome')),
                ('description', models.TextField(help_text='Preencha com a Descri\xe7\xe3o da Atividade.', max_length=256, null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('project', models.ForeignKey(verbose_name='Projeto', to='pmo.Project', help_text='Selecione um Projeto.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
