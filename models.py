# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager

from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
	_surname = models.CharField(
		max_length = 150, 
		verbose_name = "Фамилия", 
		validators=[
			RegexValidator(
				regex='^[а-яА-Я]+$',
				message='Фамилия содержит недопустимые символы!',
				code='invalid_surname'
			)
		]
	)

	_name = models.CharField(
		max_length = 150,
		verbose_name = "Имя",
		validators=[
			RegexValidator(
				regex='^[а-яА-Я]+$',
				message='Имя содержит недопустимые символы!',
				code='invalid_name'
			)
		]
	)

	_patronymic = models.CharField(
		max_length = 150, 
		verbose_name = "Отчество", 
		validators=[
			RegexValidator(
				regex='^[а-яА-Я]+$',
				message='Отчество содержит недопустимые символы!',
				code='invalid_patronymic'
			)
		]
	)

	_age = models.PositiveIntegerField(default = 0, verbose_name = "Возраст")

	@property
	def surname(self):
	    return self._surname

	@surname.setter
	def surname(self, value):
		self._surname = value

	@property
	def name(self):
	    return self._name
	
	@name.setter
	def name(self, value):
		self._name = value

	@property
	def patronymic(self):
	    return self._patronymic
	
	@patronymic.setter
	def patronymic(self, value):
		self._patronymic = value

	@property
	def age(self):
	    return self._age
	
	@age.setter
	def age(self, value):
		self._age = value

	def clean(self):
		self._surname = self._surname.capitalize()
		self._name = self._name.capitalize()
		self._patronymic = self._patronymic.capitalize()

	class Meta:
		abstract = True

class ClientManager(models.Manager):

    def deleteById(self, id):
    	obj = self.get(id = id)
    	obj.delete()

    def getById(self, id):
    	obj = self.get(id = id)
    	return obj

    def getAll(self):
    	return self.all()

class Client(Person):
	_hair = models.CharField(max_length = 20, verbose_name = "Тип волос")

	@property
	def hair(self):
	    return self._hair
	
	@hair.setter
	def hair(self, value):
		self._hair = value

	def getId(self):
		return self.id

	objects = ClientManager()

	class Meta:
		verbose_name = "Клиент"
		verbose_name_plural = "Клиенты"

	def __unicode__(self):
		return unicode(self.surname + " " + self.name + " " + self.patronymic)

class HairstyleManager(models.Manager):
    def deleteById(self, id):
    	obj = self.get(id = id)
    	obj.delete()

    def getById(self, id):
    	obj = self.get(id = id)
    	return obj

    def getAll(self):
    	return self.all()

class Hairstyle(models.Model):
	_title = models.CharField(max_length = 30, verbose_name = "Название")
	_value = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Стоимость")
	_time = models.CharField(max_length = 10, verbose_name = "Длительность")

	@property
	def title(self):
	    return self._title
	
	@title.setter
	def title(self, value):
		self._title = value

	@property
	def value(self):
	    return self._value
	
	@value.setter
	def value(self, val):
		self._value = val

	@property
	def time(self):
	    return self._time
	
	@time.setter
	def time(self, value):
		self._time = value

	def getId(self):
		return self.id

	objects = HairstyleManager()

	class Meta:
		verbose_name = "Прическа"
		verbose_name_plural = "Прически"

	def __unicode__(self):
		return unicode(self.title)

class MasterManager(models.Manager):
    def deleteById(self, id):
    	obj = self.get(id = id)
    	obj.delete()

    def getById(self, id):
    	obj = self.get(id = id)
    	return obj

    def getAll(self):
    	return self.all()

class Master(Person):
	_stage = models.CharField(max_length = 20, verbose_name = "Стаж")

	@property
	def stage(self):
	    return self._stage
	
	@stage.setter
	def stage(self, value):
		self._stage = value

	def getId(self):
		return self.id

	objects = MasterManager()

	class Meta:
		verbose_name = "Мастер"
		verbose_name_plural = "Мастера"

	def __unicode__(self):
		return unicode(self.surname + " " + self.name + " " + self.patronymic)

class OrderManager(models.Manager):
    def deleteById(self, id):
    	obj = self.get(id = id)
    	obj.delete()

    def getById(self, id):
    	obj = self.get(id = id)
    	return obj

    def getAll(self):
    	return self.all()

class Order(models.Model):
	_client = models.ForeignKey(Client)
	_master = models.ForeignKey(Master)
	_hairstyle = models.ForeignKey(Hairstyle)
	_datetime = models.DateTimeField(auto_now_add = True)

	@property
	def client(self):
	    return self._client
	
	@client.setter
	def client(self, value):
		self._client = value

	def getClientId(self):
		return self._client.id

	@property
	def master(self):
	    return self._master
	
	@master.setter
	def master(self, value):
		self._master = value

	def getMasterId(self):
		return self._master.id

	@property
	def hairstyle(self):
	    return self._hairstyle
	
	@hairstyle.setter
	def hairstyle(self, value):
		self._hairstyle = value

	def getHairstyleId(self):
		return self._hairstyle.id

	@property
	def datetime(self):
	    return self._datetime
	
	@datetime.setter
	def datetime(self, value):
		self._datetime = value

	def getId(self):
		return self.id

	objects = OrderManager()

	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"
