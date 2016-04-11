# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from models import Client, Master, Hairstyle, Order

class SomeBaseForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		for _, field in self.fields.items():
			if field.widget.is_required:
				field.widget.attrs['required'] = 'required'

class ClientEditForm(SomeBaseForm):
	class Meta:
		model = Client
		fields = '__all__'

class ClientAddForm(SomeBaseForm):
	class Meta:
		model = Client
		fields = '__all__'

class MasterEditForm(SomeBaseForm):
	class Meta:
		model = Master
		fields = '__all__'

class MasterAddForm(SomeBaseForm):
	class Meta:
		model = Master
		fields = '__all__'

class HairstyleEditForm(SomeBaseForm):
	class Meta:
		model = Hairstyle
		fields = '__all__'

class HairstyleAddForm(SomeBaseForm):
	class Meta:
		model = Hairstyle
		fields = '__all__'

class OrderEditForm(SomeBaseForm):
	class Meta:
		model = Order
		fields = '__all__'

class OrderAddForm(SomeBaseForm):
	class Meta:
		model = Order
		fields = '__all__'

class Query01Form(forms.Form):
	master = forms.ModelChoiceField(queryset=Master.objects.all())
	#value = forms.DecimalField(max_digits=10, min_value=0)

	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		#for _, field in self.fields.items():
		#	field.widget.attrs['required'] = 'required'
		self.fields['master'].widget.attrs['required'] = 'required'

'''class Query01ShowForm(forms.Form):
	pass'''

class Query02Form(forms.Form):
	client = forms.ModelChoiceField(queryset=Client.objects.all())

	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		self.fields['client'].widget.attrs['required'] = 'required'

class Query03Form(forms.Form):
	client = forms.ModelChoiceField(queryset=Client.objects.all())
	master = forms.ModelChoiceField(queryset=Master.objects.all())

	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		self.fields['client'].widget.attrs['required'] = 'required'

class Query06Form(forms.Form):
	client = forms.ModelChoiceField(queryset=Client.objects.all())

	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		self.fields['client'].widget.attrs['required'] = 'required'

class QueryFormList(object):
	queries = {
		'1' : Query01Form,
		'2' : Query02Form,
		'3' : Query03Form,
		'6' : Query06Form,
	}

	'''@staticmethod
	def getForm(key):
		return queries[key]'''