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
		all_phones = hmod.Phone.objects.all().order_by('phone_id')
	except hmod.Phone.DoesNotExist:
		print('Database contains no phones')
		#return HttpResponseRedirect('homepage/database_err')
	params['all_phones'] = all_phones

	return templater.render_to_response(request, 'phones.html' ,params)
###########################################################################
############################### Edit phone
@view_function
@permission_required('homepage.manager_check', login_url='homepage/login/')
def edit(request):
	
	params = {}
	try:
		phone = hmod.Phone.objects.get(phone_id=request.urlparams[0])
	except hmod.Phone.DoesNotExist:
		return HttpResponseRedirect('/homepage/phones/')

	form = PhoneEditForm(initial={
		'number': phone.number,
		'extension': phone.extension,
		'phone_type': phone.phone_type,
		})


	if request.method == 'POST':
		form = PhoneEditForm(request.POST)
		if form.is_valid():
			#make the changes on the user object
			phone.number = form.cleaned_data['number']
			phone.extension = form.cleaned_data['extension']
			phone.phone_type = form.cleaned_data['phone_type']
			phone.save()
			return HttpResponseRedirect('/homepage/phones/')
			

	# do some edit work here
	params['form'] = form
	params['phone'] = phone
	return templater.render_to_response(request, 'phones.edit.html' ,params)


class PhoneEditForm(forms.Form):
	number = forms.CharField(required=True, min_length=9, max_length=14)
	extension = forms.CharField(required=False, min_length=0, max_length=10)
	phone_type = forms.CharField(required=True, min_length=1, max_length=10)

############################################################################
###################### Create a phone

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def create(request):

	phone= hmod.Phone()
	phone.number = '(123)-456-7890'
	phone.extension = '2-4444'
	phone.phone_type = 'Work'
	
	phone.save()

	return HttpResponseRedirect('/homepage/phones.edit/{}/'.format(phone.phone_id))
############################################################################
################### delete a user

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def delete(request):
	try:
		phone = hmod.Phone.objects.get(phone_id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/phones/')

	phone.delete()
	return HttpResponseRedirect('/homepage/phones/'.format(phone.phone_id))
