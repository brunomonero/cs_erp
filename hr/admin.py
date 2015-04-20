#! -*- coding: utf-8 -*-
from django.contrib import admin
from hr.models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	list_display = (
		'code',
		'name',
	)
	search_fields = (
		'code',
		'name',
	)

admin.site.register(Employee, EmployeeAdmin)