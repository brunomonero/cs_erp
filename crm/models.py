#! -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Customer(models.Model):
	code =models.CharField(u'Sigla', max_length=4, blank=False, null=False, unique=True, help_text=u'Preencha com a Sigla do Cliente.') 
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome ou Razão Social do Cliente.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.name)

class Department(models.Model):
	code =models.CharField(u'Sigla', max_length=4, blank=False, null=False, unique=True, help_text=u'Preencha com a Sigla do Cliente.') 
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Cliente.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.name)	

class Contact(models.Model):
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Contato.')
	email = models.EmailField(u'Email', max_length=256, blank=False, null=False, help_text=u'Preencha com o Email do Cliente.')
	department = models.ForeignKey('Department', verbose_name=u'Departamento', blank=False, null=False, help_text=u'Selecione um Departamento.')
	customer = models.ForeignKey('Customer', verbose_name=u'Cliente', blank=False, null=False, help_text=u'Selecione um Cliente.')

	def __unicode__(self):
		return u"{0}".format(self.name)

class State(models.Model):
	code = models.CharField(u'Sigla', max_length=2, blank=False, null=False, help_text=u'Preencha com a Sigla do Estado.')
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com o Nome do Estado.')
	country = models.ForeignKey('Country', verbose_name=u'País', blank=False, null=False, help_text=u'Selecione um País.')

	def __unicode__(self):
		return u"{0} - {1} (2)".format(self.code, self.name, self.country.code)

class Country(models.Model):
	code = models.CharField(u'Sigla', max_length=3, blank=False, null=False, help_text=u'Preencha com a Sigla do País.')
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com o Nome do País.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.name)

class Address(models.Model):
	zipcode = models.CharField(u'CEP', max_length=8, blank=False, null=False, help_text=u'Preencha com CEP do Endereço.')
	street = models.CharField(u'Logradouro', max_length=8, blank=False, null=False, help_text=u'Preencha com Logradouro do Endereço.')
	number = models.PositiveIntegerField(u'Número', blank=False, null=False, default=0, help_text=u'Preencha com Número do Endereço.')
	complement = models.CharField(u'Complemento', max_length=256, blank=True, null=True, help_text=u'Preencha com o Complemento do Endereço. P.ex.: apto. 101')
	neighborhood = models.CharField(u'Bairro', max_length=256, blank=False, null=False, help_text=u'Preencha com o Bairro do Endereço.')
	city = models.CharField(u'Cidade', max_length=256, blank=False, null=False, help_text=u'Preencha com a Cidade do Endereço.')
	'''state = 
	country = '''

	def __unicode__(self):
		return u"{0}, {1} - {2}}".format(self.street, self.number, complement)