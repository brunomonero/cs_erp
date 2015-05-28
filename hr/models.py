#! -*- coding: utf-8 -*-
from django.db import models
from crm.models import Country

# Create your models here.

class Employee(models.Model):

	GENDER_CHOICES = (
		('M', 'Masculino'),
		('F', 'Feminino'),
	)

	MARITAL_STATUS_CHOICES = (
		('S', 'Solteiro'),
		('C', 'Casado'),
		('D', 'Divorciado'),
		('V', 'Viuvo')
	)

	number = models.PositiveIntegerField(u'Matrícula', blank=False, null=False, unique=True, help_text=u'Preencha a matrícula do Funcionário.')
	code = models.CharField(u'Sigla', max_length=4, blank=False, null=False, unique=True, help_text=u'Preencha com a Sigla do Funcionário.') 
	username = models.CharField(u'Usuário', max_length=100, blank=False, null=False, unique=True, help_text=u'Preencha com o nome de usuário do Funcionário.') 
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Funcionário.')
	shortname = models.CharField(u'Nome simplificado', max_length=100, blank=False, null=False, help_text=u'Preencha com um nome simplificado do Funcionário.') 
	gender = models.CharField(u'Sexo', max_length=1, choices=GENDER_CHOICES, blank=False, null=False, help_text=u'Preencha com sexo do Funcionário.')
	email_personal = models.EmailField(u'Email Pessoal', max_length=256, blank=True, null=True, help_text=u'Preencha com o Email pessoal do Funcionário.')
	birthday_date = models.DateField(u'Data de Aniversário', editable=True, auto_now=False, blank=False, null=False, auto_now_add=False, help_text=u'Preencha a data de aniversário do Funcionário no formato (dd/mm/aaaa).')
	marital_status = models.CharField(u'Estado Civil', max_length=1, choices=MARITAL_STATUS_CHOICES, blank=False, null=False, help_text=u'Preencha com estado civil do Funcionário.')
	nationality = models.ForeignKey('crm.Country', verbose_name=u'Nacionalidade', blank=False, null=False, help_text=u'Selecione a nacionalidade do Funcionário.')
	rg = models.CharField(u'Registro Civil (RG)', max_length=12, blank=False, null=False, help_text=u'Preencha com o número do registro civil do Funcionário.')
	cpf = models.CharField(u'CPF', max_length=11, blank=False, null=False, unique=True, help_text=u'Preencha com o número do cadastro de pessoa física (CPF) do Funcionário.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.shortname)

	class Meta:
		verbose_name = u'Funcionário'