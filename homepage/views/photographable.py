from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from homepage import models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
import random
from django.contrib.auth.decorators import permission_required


templater = get_renderer('homepage')

@view_function
@permission_required('homepage.is_user', login_url='homepage/login/')
def process_request(request):
	params = {}

	try:
		all_pt = hmod.PhotographableThing.objects.all().order_by('object_id')
	except hmod.PhotographableThing.DoesNotExist:
		print('Database contains no events')
		#return HttpResponseRedirect('homepage/database_err')
	params['all_pt'] = all_pt

	return templater.render_to_response(request, 'photographable.html' ,params)

##########################################################################
################### edits a single


@view_function
@permission_required('homepage.manager_check', login_url='homepage/login/')
def edit(request):
	
	params = {}
	try:
		photographable = hmod.PhotographableThing.objects.get(object_id=request.urlparams[0])
	except hmod.PhotographableThing.DoesNotExist:
		return HttpResponseRedirect('/homepage/photographable/')

	form = PhotographableEditForm(initial={
		'object_id': photographable.object_id,
		})


	if request.method == 'POST':
		form = PhotographableEditForm(request.POST)
		if form.is_valid():
			#make the changes on the user object
			photographable.object_id = form.cleaned_data['object_id']
			photographable.save()
			return HttpResponseRedirect('/homepage/photographable/')
			

	# do some edit work here
	params['form'] = form
	params['photographable'] = photographable
	return templater.render_to_response(request, 'photographable.edit.html' ,params)


class PhotographableEditForm(forms.Form):
	object_id = forms.IntegerField(required=True)

############################################################################
###################### Create a User

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def create(request):
	print(1)
	photographable= hmod.PhotographableThing()
	photographable.object_id = str(random.randint(1000001, 9999999))
	print(0)
	photographable.save()

	return HttpResponseRedirect('/homepage/photographable.edit/{}/'.format(photographable.object_id))
############################################################################
################### delete a user

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def delete(request):
	try:
		photographable = hmod.PhotographableThing.objects.get(object_id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/photographable/')

	photographable.delete()
	return HttpResponseRedirect('/homepage/photographable/'.format(photographable.object_id))	