# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from labbd.models import Order, Client, Hairstyle, Master
from forms import ClientEditForm, ClientAddForm, MasterEditForm, MasterAddForm, HairstyleEditForm, HairstyleAddForm, OrderEditForm, OrderAddForm, QueryFormList
from django.template.context_processors import csrf
#from django.db.models import Q, Sum
import time

# Create your views here.
def show(request):
	return render_to_response('labbd.html')

def show_add_order(request):
	args = {}
	args.update(csrf(request))
	args['form'] = OrderAddForm()
	return render_to_response('labbd2_add_order.html', args)

def add_order(request):
	if request.POST:
		form = OrderAddForm(request.POST)
		if form.is_valid():
			order = form.save(commit = True)
	return redirect('/labbd/orders/')

def show_orders(request):
	#!!!
	return render_to_response('labbd2_orders.html', {
		'orders' : Order.objects.all(),
		'clients' : Client.objects.all(),
		'hairstyles' : Hairstyle.objects.all(),
		'masters' : Master.objects.all(),
	})

def show_order(request, order_id):
	args = {}
	args.update(csrf(request))
	order = Order.objects.getById(order_id)
	args['order'] = order
	args['number'] = order_id
	args['client'] = order.client
	args['hairstyle'] = order.hairstyle
	args['master'] = order.master
	return render_to_response('labbd2_order.html', args)
	# args -> locals

def show_edit_order(request, order_id):
	args = {}
	args.update(csrf(request))
	#args['order'] = Order.objects.get(id = order_id)
	args['order'] = Order.objects.getById(order_id)
	args['form'] = OrderEditForm(instance = args['order'])
	return render_to_response('labbd2_edit_order.html', args)

def edit_order(request, order_id):
	if request.POST:
		#order = Order.objects.get(id = order_id)
		order = Order.objects.getById(order_id)
		form = OrderEditForm(request.POST, instance = order)
		if form.is_valid():
			form.save(commit = True)
	return redirect('/labbd/orders/%s/' % order_id)

def delete_order(request, order_id):
	if request.POST:
		#order = Order.objects.get(id = order_id)
		#order.delete()
		Order.objects.deleteById(order_id)
	return redirect('/labbd/orders/')

def show_clients(request):
	return render_to_response('labbd2_clients.html', {
		'clients' : Client.objects.getAll(),
	})

'''def show_client(request, client_id):
	return render_to_response('labbd2_client.html', {
		'client' : Client.objects.get(id = client_id),
	})
'''
def show_client(request, client_id):
	args = {}
	args.update(csrf(request))
	#args['client'] = Client.objects.get(id = client_id)
	args['client'] = Client.objects.getById(client_id)
	args['form'] = ClientEditForm(instance = args['client'])
	return render_to_response('labbd2_client.html', args)

def show_add_client(request):
	args = {}
	args.update(csrf(request))
	args['form'] = ClientAddForm
	return render_to_response('labbd2_add_client.html', args)

def add_client(request):
	if request.POST:
		form = ClientAddForm(request.POST)
		if form.is_valid():
			client = form.save(commit = True)
		else:
			args = {}
			args.update(csrf(request))
			args['form'] = form
			return render_to_response('labbd2_add_client.html', args)
	return redirect('/labbd/clients/')

def edit_client(request, client_id):
	if request.POST:
		#client = Client.objects.get(id = client_id)
		client = Client.objects.getById(client_id)
		form = ClientEditForm(request.POST, instance = client)
		if form.is_valid():
			form.save(commit = True)
			#client = form.save(commit = True)
			#client.name = Client.objects.get(id = client_id)
			#form.save()
	#return redirect('/labbd/clients/%s/' % client_id)
	return redirect('/labbd/clients/')

def delete_client(request, client_id):
	if request.POST:
		Client.objects.deleteById(client_id)
	return redirect('/labbd/clients/')

def show_hairstyles(request):
	return render_to_response('labbd2_hairstyles.html', {
		'hairstyles' : Hairstyle.objects.getAll(),
	})

'''def show_hairstyle(request, hairstyle_id):
	return render_to_response('labbd2_hairstyle.html', {
		'hairstyle' : Hairstyle.objects.get(id = hairstyle_id),
	})'''

def show_hairstyle(request, hairstyle_id):
	args = {}
	args.update(csrf(request))
	#args['hairstyle'] = Hairstyle.objects.get(id = hairstyle_id)
	args['hairstyle'] = Hairstyle.objects.getById(hairstyle_id)
	args['form'] = HairstyleEditForm(instance = args['hairstyle'])
	return render_to_response('labbd2_hairstyle.html', args)

def show_add_hairstyle(request):
	args = {}
	args.update(csrf(request))
	args['form'] = HairstyleAddForm
	return render_to_response('labbd2_add_hairstyle.html', args)

def add_hairstyle(request):
	if request.POST:
		form = HairstyleAddForm(request.POST)
		if form.is_valid():
			hairstyle = form.save(commit = True)
	return redirect('/labbd/hairstyles/')

def edit_hairstyle(request, hairstyle_id):
	if request.POST:
		#hairstyle = Hairstyle.objects.get(id = hairstyle_id)
		hairstyle = Hairstyle.objects.getById(hairstyle_id)
		form = HairstyleEditForm(request.POST, instance = hairstyle)
		if form.is_valid():
			form.save(commit = True)
	return redirect('/labbd/hairstyles/')

def delete_hairstyle(request, hairstyle_id):
	if request.POST:
		#hairstyle = Hairstyle.objects.get(id = hairstyle_id)
		#hairstyle.delete()
		Hairstyle.objects.deleteById(hairstyle_id)
	return redirect('/labbd/hairstyles/')

def show_masters(request):
	return render_to_response('labbd2_masters.html', {
		'masters' : Master.objects.getAll(),
	})

'''def show_master(request, master_id):
	return render_to_response('labbd2_master.html', {
		'master' : Master.objects.get(id = master_id),
	})'''

def show_master(request, master_id):
	args = {}
	args.update(csrf(request))
	#args['master'] = Master.objects.get(id = master_id)
	args['master'] = Master.objects.getById(master_id)
	args['form'] = MasterEditForm(instance = args['master'])
	return render_to_response('labbd2_master.html', args)

def show_add_master(request):
	args = {}
	args.update(csrf(request))
	args['form'] = MasterAddForm
	return render_to_response('labbd2_add_master.html', args)

def add_master(request):
	if request.POST:
		form = MasterAddForm(request.POST)
		if form.is_valid():
			master = form.save(commit = True)
	return redirect('/labbd/masters/')

def edit_master(request, master_id):
	if request.POST:
		#master = Master.objects.get(id = master_id)
		master = Master.objects.getById(master_id)
		form = MasterEditForm(request.POST, instance = master)
		if form.is_valid():
			form.save(commit = True)
	return redirect('/labbd/masters/')

def delete_master(request, master_id):
	if request.POST:
		#master = Master.objects.get(id = master_id)
		#master.delete()
		Master.objects.deleteById(master_id)
	return redirect('/labbd/masters/')

#!!!!!!!!!!!!!!!!!!!!!!
#ЗАПРОСЫ, СДЕЛАНЫ НЕ ОЧ
#!!!!!!!!!!!!!!!!!!!!!!
def show_queries(request):
	return render_to_response('labbd2_queries.html')

def show_query(request, query_id):
	args = {}
	args.update(csrf(request))
	args['form'] = QueryFormList.queries[query_id]
	args['number'] = query_id
	return render_to_response('labbd2_query.html', args)

def show_exec_query01(request):
	number = '1'
	if request.POST:
		#form = Query01Form(request.POST)
		form = QueryFormList.queries[number](request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			
			master = cd.get('master')

			args = {}

			_startTime = time.time()

			args['number'] = number
			args['objs'] = Order.objects.raw('''
				select "labbd_client"."id" as "id", "labbd_client"."_surname" as "surname", sum("labbd_hairstyle"."_value") as "summ"
				from "labbd_client", "labbd_order", "labbd_hairstyle"
				where "labbd_order"."_client_id" = "labbd_client"."id" 
					and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
					and "labbd_order"."_master_id" = %s 
				group by "labbd_client"."id"
			''' % master.getId())

			args['time'] = "{:.7f} sec".format(time.time() - _startTime)

	return render_to_response('labbd2_show_query01.html', args)

def show_exec_query02(request):
	number = '2'
	if request.POST:
		form = QueryFormList.queries[number](request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			
			client = cd.get('client')

			args = {}

			_startTime = time.time()

			args['number'] = number
			args['client'] = client
			args['objs'] = Order.objects.raw('''
				select "labbd_master"."id" as "id", "labbd_master"."_surname" as "surname", "labbd_master"."_stage" as "stage"
				from "labbd_client", "labbd_order", "labbd_master", "labbd_hairstyle" 
				where "labbd_order"."_master_id" = "labbd_master"."id" 
					and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
					and "labbd_order"."_client_id" = "labbd_client"."id"
					and "labbd_client"."id" = %s
				group by "labbd_master"."id"
			''' % client.getId())

			args['time'] = "{:.7f} sec".format(time.time() - _startTime)

	return render_to_response('labbd2_show_query02.html', args)

def show_exec_query03(request):
	number = '3'
	if request.POST:
		form = QueryFormList.queries[number](request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			
			client = cd.get('client')
			master = cd.get('master')

			args = {}

			_startTime = time.time()
			
			args['number'] = number
			args['client'] = client
			args['master'] = master

			args['objs'] = Order.objects.raw('''
				select "labbd_hairstyle"."id" as "id", "labbd_hairstyle"."_title" as "title"
				from "labbd_client", "labbd_order", "labbd_master", "labbd_hairstyle" 
				where "labbd_order"."_master_id" = "labbd_master"."id"
					and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
					and "labbd_order"."_client_id" = "labbd_client"."id"
					and "labbd_master"."id" = {0}
					and "labbd_client"."id" = {1}
				group by "labbd_hairstyle"."id"
			'''.format(master.getId(), client.getId()))

			args['time'] = "{:.7f} sec".format(time.time() - _startTime)

	return render_to_response('labbd2_show_query03.html', args)

def show_exec_query04(request):
	args = {}
	#!!!

	_startTime = time.time()

	args['number'] = '4'
	args['objs'] = Order.objects.raw('''
		select "labbd_master"."id" as "id", "labbd_master"."_surname" as "surname", "labbd_master"."_name" as "name", "labbd_master"."_patronymic" as "patronymic", "labbd_master"."_stage" as "stage", sum("labbd_hairstyle"."_value") as "summ"
		from "labbd_client", "labbd_order", "labbd_master", "labbd_hairstyle" 
		where "labbd_order"."_master_id" = "labbd_master"."id"
			and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
			and "labbd_order"."_client_id" = "labbd_client"."id"
		group by "labbd_master"."id"
		order by "summ" desc
		limit 1
	''')

	args['time'] = "{:.7f} sec".format(time.time() - _startTime)

	return render_to_response('labbd2_show_query04.html', args)

def show_exec_query05(request):
	args = {}

	_startTime = time.time()

	args['number'] = '5'
	args['objs'] = Order.objects.raw('''
		select "id", "surname", "countt" from 
		(select "id", "surname", count("id2") as "countt" from 
			(select "labbd_master"."id" as "id", "labbd_master"."_surname" as "surname", "labbd_master"."_stage" as "stage", "labbd_hairstyle"."id" as "id2"
			from "labbd_client", "labbd_order", "labbd_master", "labbd_hairstyle" 
			where "labbd_order"."_master_id" = "labbd_master"."id"
				and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
				and "labbd_order"."_client_id" = "labbd_client"."id"
			group by "labbd_master"."id", "labbd_hairstyle"."id") as "subquery"
		group by "id", "surname") as "subquery2"
		where "countt" = (select count("labbd_hairstyle"."id") from "labbd_hairstyle")
	''')

	args['time'] = "{:.7f} sec".format(time.time() - _startTime)

	return render_to_response('labbd2_show_query05.html', args)

def show_exec_query06(request):
	number = '6'
	if request.POST:
		form = QueryFormList.queries[number](request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			
			client = cd.get('client')

			args = {}

			_startTime = time.time()

			args['number'] = number
			args['client'] = client

			args['objs'] = Order.objects.raw('''
				select "labbd_hairstyle"."_title" as "title", "labbd_hairstyle"."id" 
				from "labbd_hairstyle"
				except
				select "labbd_hairstyle"."_title" as "title", "labbd_hairstyle"."id"
				from "labbd_client", "labbd_order", "labbd_hairstyle", "labbd_master"
				where "labbd_order"."_client_id" = "labbd_client"."id" 
					and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
					and "labbd_order"."_master_id" = "labbd_master"."id"
					and "labbd_client"."id" = %s
				group by "labbd_client"."id", "labbd_hairstyle"."_title", "labbd_hairstyle"."id"
			''' % client.getId())

			args['time'] = "{:.7f} sec".format(time.time() - _startTime)

	return render_to_response('labbd2_show_query06.html', args)

def show_exec_query07(request):
	args = {}

	args['number'] = '7'

	_startTime = time.time()

	args['objs'] = Order.objects.raw('''
		select "id", "surname", "summ" from 
			(select "labbd_client"."id" as "id", "labbd_client"."_surname" as "surname", sum("labbd_hairstyle"."_value") as "summ"
			from "labbd_client", "labbd_order", "labbd_hairstyle", "labbd_master"
			where "labbd_order"."_client_id" = "labbd_client"."id" 
				and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
				and "labbd_order"."_master_id" = "labbd_master"."id"
				and "labbd_client"."id" = "labbd_client"."id"
			group by "labbd_client"."id") as "subquery"
		where "summ" = (select max("summ") from 
			(select "labbd_client"."id" as "id", "labbd_client"."_surname" as "surname", sum("labbd_hairstyle"."_value") as "summ"
			from "labbd_client", "labbd_order", "labbd_hairstyle", "labbd_master"
			where "labbd_order"."_client_id" = "labbd_client"."id" 
				and "labbd_order"."_hairstyle_id" = "labbd_hairstyle"."id" 
				and "labbd_order"."_master_id" = "labbd_master"."id"
				and "labbd_client"."id" = "labbd_client"."id"
			group by "labbd_client"."id") as "subquery")
	''')

	args['time'] = "{:.7f} sec".format(time.time() - _startTime)

	return render_to_response('labbd2_show_query07.html', args)