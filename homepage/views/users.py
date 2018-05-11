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
###############################################################
########### shows list of users
@view_function
@permission_required('homepage.check_user', login_url='/homepage/login/')
def process_request(request):

	params = {}

	try:
		all_users = hmod.User.objects.all().order_by('id')
	except hmod.User.DoesNotExist:
		print('Database contains no users')
		#return HttpResponseRedirect('homepage/database_err')
	params['all_users'] = all_users

	return templater.render_to_response(request, 'users.html' ,params)


##########################################################################
################### edits a single


@view_function
@permission_required('homepage.check_manager', login_url='/homepage/login/')
def edit(request):
	
	params = {}
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/users/')

	form = UserEditForm(initial={
		'username': user.username,
		'password': user.password,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		})


	if request.method == 'POST':
		form = UserEditForm(request.POST)
		form.userid = user.id
		if form.is_valid():
			#make the changes on the user object
			user.username = form.cleaned_data['username']
			user.set_password(form.cleaned_data['password'])
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.save()
			return HttpResponseRedirect('/homepage/users/')
			

	# do some edit work here
	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'users.edit.html' ,params)


class UserEditForm(forms.Form):
	username = forms.CharField(required=True, min_length=1, max_length=100)
	password = forms.CharField(label="Password",widget=forms.PasswordInput)
	first_name = forms.CharField(required=True, min_length=1, max_length=100)
	last_name = forms.CharField(required=True, min_length=1, max_length=100)
	email = forms.EmailField(required=True, min_length=1, max_length=100)

	def clean_username(self):
		users_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
		if users_count >= 1:	
			raise forms.ValidationError("This username is already taken.")
		
		return self.cleaned_data['username']


############################################################################
###################### Create a User

@view_function
@permission_required('homepage.check_admin', login_url='/homepage/login/')
def create(request):

	user= hmod.User()
	user.username = str(random.randint(1000001, 9999999))
	user.password = 'password'
	user.first_name = 'First Name'
	user.last_name = 'Last Name'
	user.email = 'Email@email.com'
	
	user.save()

	return HttpResponseRedirect('/homepage/users.edit/{}/'.format(user.id))
############################################################################
################### delete a user

@view_function
@permission_required('homepage.check_admin', login_url='/homepage/login/')
def delete(request):
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/users/')

	user.delete()
	return HttpResponseRedirect('/homepage/users/'.format(user.id))
