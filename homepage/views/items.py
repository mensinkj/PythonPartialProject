
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from homepage import models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth.decorators import permission_required

templater = get_renderer('homepage')

@view_function
@permission_required('homepage.is_user', login_url='homepage/login/')
def process_request(request):
	params = {}

	try:
		all_items = hmod.Item.objects.all().order_by('name')
	except hmod.Item.DoesNotExist:
		print('Database contains no items')
		#return HttpResponseRedirect('homepage/database_err')
	params['all_items'] = all_items

	return templater.render_to_response(request, 'items.html' ,params)
###########################################################################
############################### Edit Item
@view_function
@permission_required('homepage.manager_check', login_url='homepage/login/')
def edit(request):
	
	params = {}
	try:
		item = hmod.Item.objects.get(object_id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')

	form = ItemEditForm(initial={
		'name': item.name,
		'description': item.description,
		'value': item.value,
		'standard_rental_price': item.standard_rental_price,
		})


	if request.method == 'POST':
		form = ItemEditForm(request.POST)
		if form.is_valid():
			#make the changes on the user object
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.standard_rental_price = form.cleaned_data['standard_rental_price']
			item.save()
			return HttpResponseRedirect('/homepage/items/')
			

	# do some edit work here
	params['form'] = form
	params['item'] = item
	return templater.render_to_response(request, 'items.edit.html' ,params)


class ItemEditForm(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=True, min_length=1, max_length=200)
	value = forms.DecimalField(required=True, max_digits=10, decimal_places=2)
	standard_rental_price = forms.DecimalField(required=True, max_digits=10, decimal_places=2)

############################################################################
###################### Create a User

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def create(request):

	item= hmod.Item()
	item.name = 'name'
	item.description = 'this is a description of the item'
	item.value = '59.99'
	item.standard_rental_price = '17.99'
	
	item.save()

	return HttpResponseRedirect('/homepage/items.edit/{}/'.format(item.object_id))
############################################################################
################### delete a user

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def delete(request):
	try:
		item = hmod.Item.objects.get(object_id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/items/')

	item.delete()
	return HttpResponseRedirect('/homepage/items/'.format(item.object_id))