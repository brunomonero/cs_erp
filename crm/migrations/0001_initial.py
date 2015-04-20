# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(help_text='Preencha com CEP do Endere\xe7o.', max_length=8, verbose_name='CEP')),
                ('street', models.CharField(help_text='Preencha com Logradouro do Endere\xe7o.', max_length=512, verbose_name='Logradouro')),
                ('number', models.PositiveIntegerField(default=0, help_text='Preencha com N\xfamero do Endere\xe7o.', verbose_name='N\xfamero')),
                ('additional', models.CharField(help_text='Preencha com o Complemento do Endere\xe7o. P.ex.: apto. 101', max_length=256, null=True, verbose_name='Complemento', blank=True)),
                ('city', models.CharField(help_text='Preencha com a Cidade do Endere\xe7o.', max_length=256, verbose_name='Cidade')),
                ('neighborhood', models.CharField(help_text='Preencha com o Bairro do Endere\xe7o.', max_length=256, verbose_name='Bairro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Preencha com Nome do Contato.', max_length=256, verbose_name='Nome')),
                ('position', models.CharField(help_text='Preencha com o Cargo do Contato.', max_length=256, verbose_name='Cargo')),
                ('email', models.EmailField(help_text='Preencha com o Email do Cliente.', max_length=256, verbose_name='Email')),
                ('phone', models.CharField(help_text='Preencha com o Telefone do Contato.', max_length=256, verbose_name='Telefone')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='Preencha com a Sigla do Pa\xeds.', max_length=3, verbose_name='Sigla')),
                ('name', models.CharField(help_text='Preencha com o Nome do Pa\xeds.', max_length=256, verbose_name='Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='Preencha com a Sigla do Cliente.', unique=True, max_length=4, verbose_name='Sigla')),
                ('name', models.CharField(help_text='Preencha com Nome ou Raz\xe3o Social do Cliente.', max_length=256, verbose_name='Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='Preencha com a Sigla do Cliente.', unique=True, max_length=4, verbose_name='Sigla')),
                ('name', models.CharField(help_text='Preencha com Nome do Cliente.', max_length=256, verbose_name='Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text='Preencha com a Sigla do Estado.', max_length=2, verbose_name='Sigla')),
                ('name', models.CharField(help_text='Preencha com o Nome do Estado.', max_length=256, verbose_name='Nome')),
                ('country', models.ForeignKey(blank=True, to='crm.Country', help_text='Selecione um Pa\xeds.', null=True, verbose_name='Pa\xeds')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contact',
            name='customer',
            field=models.ForeignKey(blank=True, to='crm.Customer', help_text='Selecione um Cliente.', null=True, verbose_name='Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='department',
            field=models.ForeignKey(verbose_name='Departamento', to='crm.Department', help_text='Selecione um Departamento.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(blank=True, to='crm.Country', help_text='Selecione um Pa\xeds.', null=True, verbose_name='Pa\xeds'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(blank=True, to='crm.Customer', help_text='Selecione um Cliente.', null=True, verbose_name='Cliente'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(blank=True, to='crm.State', help_text='Selecione um Estado.', null=True, verbose_name='Estado'),
            preserve_default=True,
        ),
    ]
