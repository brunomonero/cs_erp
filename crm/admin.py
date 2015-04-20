#! -*- coding: utf-8 -*-
from django.contrib import admin
from crm.models import *

# Register your models here.

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0
    fields = ('zipcode', 
    	'street', 
    	'number', 
    	'additional',
    	'country',
    	'state', 
    	'city',
    	'neighborhood')

class ContactInline(admin.TabularInline):
	model = Contact
	extra = 0
	fields =(
		'name',
		'department',
		'position',
		'email',
		'phone'
	)

class CustomerAdmin(admin.ModelAdmin):
	list_display = (
		'code',
		'name'
	)
	search_fields = (
		'code', 
		'name',
	)
	inlines = [
		ContactInline,
		AddressInline
	]

class DepartmentAdmin(admin.ModelAdmin):
	list_display = (
		'code',
		'name'
	)
	search_fields = (
		'code',
		'name'
	)
	list_editable = (
		'name',
	)

class CountryAdmin(admin.ModelAdmin):
	list_display = (
		'code',
		'name'
	)
	search_fields = (
		'code', 
		'name',
	)

class StateAdmin(admin.ModelAdmin):
	list_display = (
		'country',
		'code',
		'name'
	)
	search_fields = (
		'country',
		'code', 
		'name',
	)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)

'''admin.site.register(State, StateAdmin)'''