#! -*- coding: utf-8 -*-
from django.contrib import admin
from pmo.models import *

# Register your models here.

class TaskInline(admin.TabularInline):
	model = Task
	extra = 0
	fields = (
		'name',
		'description',
	)

class TaskAdmin(admin.ModelAdmin):
	list_display = (
		'project',
		'code',
		'name',
	)
	search_fields = (
		'project',
		'code',
		'name',	
		'description'
	)

class ProjectAdmin(admin.ModelAdmin):
	list_display = (
		'customer',
		'code',
		'name',
		'type',
		'status',
	)
	search_fields = (
		'customer',
		'code',
		'name',
	)
	list_filter = (
		'type',
		'status',
	)
	inlines = (
		TaskInline,
	)

admin.site.register(Task, TaskAdmin)
admin.site.register(Project, ProjectAdmin)