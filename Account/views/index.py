from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from django.http import HttpResponse, HttpResponseRedirect, Http404
from homepage import models as hmod
from django.http import HttpRequest
from django import forms
import random
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

templater = get_renderer('Account')

@view_function
def process_request(request):
#	params = prepare_params(request)

	return templater.render_to_response(request,'index.html')

@view_function
def check_username(request):

	username1 = request.REQUEST.get('u')

	#check to see if in database (using hmod.User.object.get())
	#make sure you take care of the case where I set my own
	#username to the same username

	#users_count = hmod.User.objects.filter(username1).exclude(id=self.userid).count()
	usertaken = hmod.User.objects.filter(username = username1).exists()
	if usertaken == True:	
		return HttpResponse('fail')
	else:
		return HttpResponse('pass')

@view_function
def create(request):

	user= hmod.User()
	user.username = str(random.randint(1000001, 9999999))
	user.password = 'password'
	user.first_name = 'First Name'
	user.last_name = 'Last Name'
	user.email = 'Email@email.com'
	
	user.save()

	return HttpResponseRedirect('/Account/index.edit/{}/'.format(user.id))
	
@view_function
def edit(request):
	
	params = {}
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/Account/index/')

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

			user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
			login(request,user)

			return HttpResponseRedirect('/Account/index.edituser/{}/'.format(user.id))
			

	# do some edit work here
	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'createuser.html' ,params)


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

class UserEditForm2(forms.Form):
	username = forms.CharField(required=True, min_length=1, max_length=100)
	first_name = forms.CharField(required=True, min_length=1, max_length=100)
	last_name = forms.CharField(required=True, min_length=1, max_length=100)
	email = forms.EmailField(required=True, min_length=1, max_length=100)

	def clean_username(self):
		users_count = hmod.User.objects.filter(username=self.cleaned_data['username']).exclude(id=self.userid).count()
		if users_count >= 1:	
			raise forms.ValidationError("This username is already taken.")
		
		return self.cleaned_data['username']

class passwordform(forms.Form):
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password Confirm",widget=forms.PasswordInput)

	def clean_password2(self):
		
		if self.cleaned_data['password1'] != self.cleaned_data['password2']:
			raise forms.ValidationError("Passwords do not match")
		
		return self.cleaned_data['password2']

@view_function
def delete(request):
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/homepage/index/')

	user.delete()
	return HttpResponseRedirect('/homepage/index/'.format(user.id))

@view_function
def edituser(request):
	
	params = {}
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/index/')

	form = UserEditForm2(initial={
		'username': user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email': user.email,
		})

	if request.method == 'POST':
		form = UserEditForm2(request.POST)
		form.userid = user.id
		if form.is_valid():
			#make the changes on the user object
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.save()
			return HttpResponseRedirect('/Account/index.edituser/{}/'.format(user.id))

	# do some edit work here
	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'index.html' ,params)

@view_function
def password(request):

	params = {}
	try:
		user = hmod.User.objects.get(id=request.urlparams[0])
	except hmod.User.DoesNotExist:
		return HttpResponseRedirect('/homepage/index/')

	form = passwordform()

	if request.method == 'POST':
		form = passwordform(request.POST)
		if form.is_valid():
			
			return HttpResponseRedirect('/password_reset/')

	# do some edit work here
	params['form'] = form
	params['user'] = user
	return templater.render_to_response(request, 'password.html' ,params)


