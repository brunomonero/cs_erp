from django.db import models

# Create your models here.

class Department(models.Model):
	code =models.CharField(u'Sigla', max_length=4, blank=False, null=False, unique=True, help_text=u'Preencha com a Sigla do Cliente.') 
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Cliente.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.name)	

class Contact(models.Model):
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome do Contato.')
	email = models.EmailField(u'Email', max_length=256, blank=False, null=False, help_text=u'Preencha com o Email do Cliente.')
	department = models.ForeignKey('Department', verbose_name=u'Departamento', blank=False, null=False, help_text=u'Selecione um Departamento.')

	def __unicode__(self):
		return u"{0}".format(self.name)

class Customer(models.Model):
	code =models.CharField(u'Sigla', max_length=4, blank=False, null=False, unique=True, help_text=u'Preencha com a Sigla do Cliente.') 
	name = models.CharField(u'Nome', max_length=256, blank=False, null=False, help_text=u'Preencha com Nome ou Razão Social do Cliente.')
	contact = models.ForeignKey('Contact', verbose_name=u'Contato', blank=False, null=False, help_text='Selecione um contato.')

	def __unicode__(self):
		return u"{0} - {1}".format(self.code, self.name)