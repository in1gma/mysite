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