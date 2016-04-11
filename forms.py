# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import Client, Master, Hairstyle, Order

class ClientEditForm(ModelForm):
	class Meta:
		model = Client
		fields = '__all__'

class ClientAddForm(SomeBaseForm):
	class Meta:
		model = Client
		fields = '__all__'

class MasterEditForm(ModelForm):
	class Meta:
		model = Master
		fields = '__all__'

class MasterAddForm(ModelForm):
	class Meta:
		model = Master
		fields = '__all__'

class HairstyleEditForm(ModelForm):
	class Meta:
		model = Hairstyle
		fields = '__all__'

class HairstyleAddForm(ModelForm):
	class Meta:
		model = Hairstyle
		fields = '__all__'

class OrderEditForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class OrderAddForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
