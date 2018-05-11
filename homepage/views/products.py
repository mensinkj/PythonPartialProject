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
		all_products = hmod.Product.objects.all().order_by('name')
	except hmod.Product.DoesNotExist:
		print('Database contains no products')
		#return HttpResponseRedirect('homepage/database_err')
	params['all_products'] = all_products

	return templater.render_to_response(request, 'products.html' ,params)

###########################################################################
############################### Edit Product
@view_function
@permission_required('homepage.manager_check', login_url='homepage/login/')
def edit(request):
	
	params = {}
	try:
		product = hmod.Product.objects.get(object_id=request.urlparams[0])
	except hmod.Product.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')

	form = ProductEditForm(initial={
		'name': product.name,
		'description': product.description,
		'category': product.category,
		'current_price': product.current_price,
		})


	if request.method == 'POST':
		form = ProductEditForm(request.POST)
		if form.is_valid():
			#make the changes on the user object
			product.name = form.cleaned_data['name']
			product.description = form.cleaned_data['description']
			product.category = form.cleaned_data['category']
			product.current_price = form.cleaned_data['current_price']
			product.save()
			return HttpResponseRedirect('/homepage/products/')
			

	# do some edit work here
	params['form'] = form
	params['product'] = product
	return templater.render_to_response(request, 'products.edit.html' ,params)


class ProductEditForm(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=True, min_length=1, max_length=200)
	category = forms.CharField(required=True, min_length=1, max_length=100)
	current_price = forms.DecimalField(required=True, max_digits=10, decimal_places=2)

############################################################################
###################### Create a User

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def create(request):

	product= hmod.Product()
	product.name = 'name'
	product.description = 'this is a description of the product'
	product.category = 'category'
	product.current_price = '17.99'
	
	product.save()

	return HttpResponseRedirect('/homepage/products.edit/{}/'.format(product.object_id))
############################################################################
################### delete a user

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def delete(request):
	try:
		product = hmod.Product.objects.get(object_id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/products/')

	product.delete()
	return HttpResponseRedirect('/homepage/products/'.format(product.object_id))