# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(help_text='Preencha a matr\xedcula do Funcion\xe1rio.', unique=True, verbose_name='Matr\xedcula')),
                ('code', models.CharField(help_text='Preencha com a Sigla do Funcion\xe1rio.', unique=True, max_length=4, verbose_name='Sigla')),
                ('username', models.CharField(help_text='Preencha com o nome de usu\xe1rio do Funcion\xe1rio.', unique=True, max_length=100, verbose_name='Usu\xe1rio')),
                ('name', models.CharField(help_text='Preencha com Nome do Funcion\xe1rio.', max_length=256, verbose_name='Nome')),
                ('shortname', models.CharField(help_text='Preencha com um nome simplificado do Funcion\xe1rio.', max_length=100, verbose_name='Nome simplificado')),
                ('gender', models.CharField(help_text='Preencha com sexo do Funcion\xe1rio.', max_length=1, verbose_name='Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('email_personal', models.EmailField(help_text='Preencha com o Email pessoal do Funcion\xe1rio.', max_length=256, null=True, verbose_name='Email Pessoal', blank=True)),
                ('birthday_date', models.DateField(help_text='Preencha a data de anivers\xe1rio do Funcion\xe1rio no formato (dd/mm/aaaa).', verbose_name='Data de Anivers\xe1rio')),
                ('marital_status', models.CharField(help_text='Preencha com estado civil do Funcion\xe1rio.', max_length=1, verbose_name='Estado Civil', choices=[(b'S', b'Solteiro'), (b'C', b'Casado'), (b'D', b'Divorciado'), (b'V', b'Viuvo')])),
                ('nationality', models.ForeignKey(blank=True, to='crm.Country', help_text='Selecione a nacionalidade do Funcion\xe1rio.', null=True, verbose_name='Nacionalidade')),
            ],
            options={
                'verbose_name': 'Funcion\xe1rio',
            },
            bases=(models.Model,),
        ),
    ]
