#! -*- coding: utf-8 -*-
from django.contrib import admin
from sales.models import *

# Register your models here.

class PriceListInline(admin.TabularInline):
    model = PriceList
    extra = 0
    fields = (
    	'function',
    	'price'
	)

class FunctionAdmin(admin.ModelAdmin):
	list_display = (
		'name',
	)
	search_fields = (
		'name',
	)

class ContractAdmin(admin.ModelAdmin):
	list_display = (
		'customer',
		'name',
		'initial_date',
		'finish_date',
	)
	search_fields = (
		'customer',
		'name',
		'initial_date',
		'finish_date',
	)
	inlines = [
		PriceListInline
	]

admin.site.register(Function, FunctionAdmin)
admin.site.register(Contract, ContractAdmin)