#! -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Employee(models.Model):
	code = models.CharField(u'Sigla', max_length=4, blank=False, null=False, unique=True, help_text=u'Preencha com a Sigla do Cliente.') 
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Cliente.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.name)