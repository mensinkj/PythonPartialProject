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
		all_areas = hmod.Area.objects.all().order_by('object_id')
	except hmod.Area.DoesNotExist:
		print('Database contains no areas')
		#return HttpResponseRedirect('homepage/database_err')
	params['all_areas'] = all_areas

	return templater.render_to_response(request, 'areas.html' ,params)

##########################################################################
################### edits a single


@view_function
@permission_required('homepage.manager_check', login_url='homepage/login/')
def edit(request):
	
	params = {}
	try:
		area = hmod.Area.objects.get(object_id=request.urlparams[0])
	except hmod.Area.DoesNotExist:
		return HttpResponseRedirect('/homepage/areas/')

	form = AreaEditForm(initial={
		'object_id': area.object_id,
		'name': area.name,
		'description': area.description,
		'place_number': area.place_number,
		})


	if request.method == 'POST':
		form = AreaEditForm(request.POST)
		if form.is_valid():
			#make the changes on the area object
			area.object_id = form.cleaned_data['object_id']
			area.name = form.cleaned_data['name']
			area.description = form.cleaned_data['description']
			area.place_number = form.cleaned_data['place_number']
			area.save()
			return HttpResponseRedirect('/homepage/areas/')
			

	# do some edit work here
	params['form'] = form
	params['area'] = area
	return templater.render_to_response(request, 'areas.edit.html' ,params)


class AreaEditForm(forms.Form):
	object_id = forms.IntegerField(required=True)
	name = forms.CharField(required=True, min_length=1, max_length=100)
	description = forms.CharField(required=True, min_length=1, max_length=200)
	place_number = forms.IntegerField(required=True)

############################################################################
###################### Create a area

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def create(request):

	area= hmod.Area()
	area.object_id = str(random.randint(1000001, 9999999))
	area.name = 'Area Name'
	area.description = 'This is a description of the area'
	area.place_number =  str(random.randint(10001, 99999))
	
	area.save()

	return HttpResponseRedirect('/homepage/areas.edit/{}/'.format(area.object_id))
############################################################################
################### delete a area

@view_function
@permission_required('homepage.admin_check', login_url='/homepage/login/')
def delete(request):
	try:
		area = hmod.Area.objects.get(object_id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/areas/')

	area.delete()
	return HttpResponseRedirect('/homepage/areas/'.format(area.object_id))