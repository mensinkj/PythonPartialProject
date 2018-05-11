from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from homepage import models as hmod
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django import forms
import requests
from django.core import mail
from django.core.mail import send_mail

templater = get_renderer('shopping')

@view_function
def process_request(request):
#	params = prepare_params(request)
	
	params = {}
	
	try:
		catalog_items = hmod.ProductSpecification.objects.all()
	except hmod.ProductSpecification.DoesNotExist:
		print('Database contains no Products')

	params['catalog_items'] = catalog_items
	return templater.render_to_response(request,'index.html',params)
	
@view_function
def checkout(request):
#	params = prepare_params(request)
	
	params = {}
	
	form = checkoutform()

	if request.method == 'POST':
		form = checkoutform(request.POST)
		if form.is_valid():
			API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
			API_KEY = 'dcda4e87c67ada2cd111032aaf259bae'
			amount = form.cleaned_data['amount']
			credit_card_type = form.cleaned_data['credit_card_type']
			credit_card_number= form.cleaned_data['credit_card_number']
			cc_exp_month = form.cleaned_data['cc_exp_month']
			cc_exp_year =form.cleaned_data['cc_exp_year']
			cvc = form.cleaned_data['cvc']
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			r = requests.post(API_URL, data={
				'apiKey': API_KEY,
				'currency': 'usd',
				'amount': amount,
				'type': 'visa',
				'number': '4732817300654',
				'exp_month': '10',
				'exp_year' : '15',
				'cvc': '411',
				'name': 'Cosmo Limesandal',
				'description': description,
				})

			#just for debugging, print the response text
			print(r.text)

			#parse the response to a dictionary
			resp = r.json() 
			if 'error' in resp:
				print("ERROR: ", resp['error'])

			else:
				print(resp.keys())
				print(resp['ID'])
				connection = mail.get_connection()
				connection.open()
				email = mail.EmailMessage('Colonial Heritage Foundation', 'Thank you for your purchase!!!!', 'joshuamensink@gmail.com',
                          ['joshua@mensink.name'], connection=connection)
				email.send()

			return HttpResponseRedirect('/shopping/receipt/', params)
	
	params['form'] = form
	return templater.render_to_response(request, 'checkout.html' ,params)

class checkoutform(forms.Form):
	name = forms.CharField(required=True, min_length=1, max_length=100)
	address = forms.CharField(required=True, min_length=1, max_length=100)
	Street = forms.CharField(required=True, min_length=1, max_length=100)
	city = forms.CharField(required=True, min_length=1, max_length=100)
	state= forms.CharField(required=True, min_length=1, max_length=100)
	zip_code = forms.CharField(required=True, min_length=1, max_length=100)
	amount = forms.DecimalField(max_digits=10, decimal_places=2)
	credit_card_type = forms.CharField(required=True, min_length = 1, max_length = 100)
	credit_card_number = forms.IntegerField(required=True)
	cc_exp_month = forms.CharField(required=True, min_length = 1, max_length = 100)
	cc_exp_year = forms.CharField(required=True, min_length = 1, max_length = 100)
	cvc = forms.CharField(required=True, min_length = 1, max_length = 100)
	description=forms.CharField(required=True, min_length = 1, max_length = 100)



@view_function
def payment(request):


#send the request with the data
	API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
	API_KEY = 'dcda4e87c67ada2cd111032aaf259bae'

	r = requests.post(API_URL, data={
		'apiKey': API_KEY,
		'currency': 'usd',
		'amount': '5.99',
		'type': 'Visa',
		'number': '4732817300654',
		'exp_month': '10',
		'exp_year' : '15',
		'cvc': '411',
		'name': 'Cosmo Limesandal',
		'description': 'Charge for cosmo@is411.byu.edu',
		})

	#just for debugging, print the response text
	print(r.text)

	#parse the response to a dictionary
	resp = r.json()
	if 'error' in resp:
		print("ERROR: ", resp['error'])

	else:
		print(resp.keys())
		print(resp['ID'])
# @view_function
# def additem(request):

# 	params = {}

# 	#add to the shooping cart
# 	item = hmod.ProductSpecification.objects.get(id=request.urlparams[0])
# 	#make sure that we have a shopping cart in the session		
# 	if 'shopping_cart' not in request.session:
# 		request.session['shopping_cart'] = {}
# 	#add the item to the shopping cart
# 	if item.id in request.session['shopping_cart']:
# 		request.session['shopping_cart'][item.id] += 1
# 	else:
# 		request.session['shopping_cart'][item.id] = 1

# 	return templater.render_to_response(request,'index.html',params)

@view_function
def search(request):
	params = {}

	products = hmod.ProductSpecification.objects.filter(name__icontains=request.urlparams[0])
	
	productCount = hmod.ProductSpecification.objects.filter(name__icontains=request.urlparams[0]).count()
	
	params['products'] = products
	params['productCount'] = productCount
	
	return templater.render_to_response(request, 'index.search.html', params)

