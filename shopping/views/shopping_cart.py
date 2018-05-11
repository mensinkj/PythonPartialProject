from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from homepage import models as hmod
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms

templater = get_renderer('shopping')

@view_function
def process_request(request):
#	params = prepare_params(request)
	
	params = {}

	#show the shopping cart in an ajax dialog

	return templater.render_to_response(request, 'shopping_cart.html', params)

@view_function
def additem(request):


	params = {}

	products = hmod.ProductSpecification.objects.get(id=request.urlparams[0])

	pid = request.urlparams[0]
	qty = request.urlparams[1]

	if 'shopping_cart' not in request.session:
		request.session['shopping_cart'] = {}

	if pid in request.session['shopping_cart']:
		request.session['shopping_cart'][pid] += qty
	else:
		request.session['shopping_cart'][pid] = qty

	print(request.session['shopping_cart'][pid])


	product_list = []
	quantity_list = []
	for k,v in request.session['shopping_cart'].items():
		product_object = hmod.ProductSpecification.objects.get(id=k)
		quantity = int(v)
		quantity_list.append(quantity)
		product_list.append(product_object)



	# if request.method == 'POST':
	# 	form = shoppingform(request.POST)
	# 	if form.is_valid():
	# 	#make the changes on the user object
	# 		pid = form.cleaned_data['product']
	# 		qty = form.cleaned_data['qty']

	# 	user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
	# 	login(request,user)

	# 	return HttpResponseRedirect('/Account/index.edituser/{}/'.format(user.id))

	params['items'] = product_list
	params['qty'] = quantity_list
	return templater.render_to_response(request,'shopping_cart.html', params)

@view_function
def delete(request):


	params = {}
	print('>>>>>>>>>>>>>1')
	del request.session['shopping_cart']
	print('>>>>>>>>>>>>>>2')

	return HttpResponseRedirect('/shopping/index/')