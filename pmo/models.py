#! -*- coding: utf-8 -*-
from django.db import models
from crm.models import *

# Create your models here.

class Task(models.Model):
	project = models.ForeignKey('Project', verbose_name=u'Projeto', blank=False, null=False, help_text=u'Selecione um Projeto.')
	code = models.AutoField(u'Código', primary_key=True, help_text=u'Código da Atividade.')
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Atividade.')
	description = models.TextField(u'Descrição', max_length=256, blank=True, null=True, help_text=u'Preencha com a Descrição da Atividade.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.name)

	class Meta:
		verbose_name = u'Tarefa'

class Project(models.Model):
	PROJECT_TYPE_CHOICES = (
		('HM', 'Horas e Materiais'),
		('EF', 'Escopo Fechado'),
	)
	PROJECT_STATUS_CHOICES = (
		('AB', 'Aberto'),
		('EP', 'Em progresso'),
		('CO', u'Concluído'),
		('CA', 'Cancelado'),
	)
	customer = models.ForeignKey('crm.Customer', verbose_name=u'Cliente', blank=False, null=False, help_text=u'Selecione um Cliente.')
	code = models.CharField(u'Sigla', max_length=4, blank=False, null=False, unique=True, help_text=u'Preencha com a Sigla do Cliente.') 
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Cliente.')
	type = models.CharField(u'Tipo', max_length=2, choices=PROJECT_TYPE_CHOICES, blank=False, null=False, help_text=u'Selecione um tipo.')
	status = models.CharField(u'Status', max_length=2, default='AB', choices=PROJECT_STATUS_CHOICES, blank=False, null=False, help_text=u'Selecione um Status.')

	def __unicode__(self):
		return u"{0} - {1} (2)".format(self.code, self.name, self.customer.name)

	class Meta:
		verbose_name = u'Projeto'