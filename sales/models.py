#! -*- coding: utf-8 -*-
from django.db import models
from crm.models import Customer

# Create your models here.

class Contract(models.Model):
	customer = models.ForeignKey('crm.Customer', verbose_name=u'Cliente', blank=True, null=True, help_text=u'Selecione um Cliente.')
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Contrato.')
	initial_date = models.DateField(u'Data de Início', auto_now=False, auto_now_add=True, help_text=u'Selecione uma data de início de vigência do Contrato.')
	finish_date = models.DateField(u'Data de Término', auto_now=False, auto_now_add=True, help_text=u'Selecione uma data de término de vigência do Contrato.')

	def __unicode__(self):
		return u"{0} ({1})".format(self.name, self.customer.name)

	class Meta:
		verbose_name = u'Contrato'

class Function(models.Model):
	name = models.CharField(u'Função', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome da Função.')

	def __unicode__(self):
		return u"{0}".format(self.name)

	class Meta:
		verbose_name = u'Função'
		verbose_name_plural = u'Funções'

class PriceList(models.Model):
	contract = models.ForeignKey('Contract', verbose_name=u'Contrato', blank=False, null=False, help_text=u'Selecione um Contrato.')
	function = models.ForeignKey('Function', verbose_name=u'Função', blank=False, null=False, help_text=u'Selecione uma Função.')
	price = models.DecimalField(u'Preço', max_digits=5, decimal_places=2, blank=False, null=False, help_text=u'Preencha com o Preço da Função.')

	def __unicode__(self):
		return u"{0}".format(self.name)

	class Meta:
		verbose_name = u'Lista de Preços'
		verbose_name_plural = u'Listas de Preços'