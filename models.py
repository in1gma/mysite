# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Client(models.Model):
	surname = models.CharField(max_length = 150, verbose_name = "Фамилия")
	name = models.CharField(max_length = 150, verbose_name = "Имя")
	patronymic = models.CharField(max_length = 150, verbose_name = "Отчество")
	age = models.PositiveIntegerField(default = 0, verbose_name = "Возраст")
	hair = models.CharField(max_length = 20, verbose_name = "Тип волос")

	def __unicode__(self):
		return unicode(self.surname + " " + self.name + " " + self.patronymic)

class Hairstyle(models.Model):
	title = models.CharField(max_length = 30, verbose_name = "Название")
	value = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = "Стоимость")
	time = models.CharField(max_length = 10, verbose_name = "Длительность")

	def __unicode__(self):
		return unicode(self.title)

class Master(models.Model):
	surname = models.CharField(max_length = 150, verbose_name = "Фамилия")
	name = models.CharField(max_length = 150, verbose_name = "Имя")
	patronymic = models.CharField(max_length = 150, verbose_name = "Отчество")
	stage = models.CharField(max_length = 20, verbose_name = "Стаж")

	def __unicode__(self):
		return unicode(self.surname + " " + self.name + " " + self.patronymic)

class Order(models.Model):
	client = models.ForeignKey(Client)
	master = models.ForeignKey(Master)
	hairstyle = models.ForeignKey(Hairstyle)
	datatime = models.DateTimeField(auto_now_add = True)