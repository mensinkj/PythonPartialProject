from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from homepage import models as hmod
from django_mako_plus.controller.router import get_renderer
from django import forms
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
import traceback

templater = get_renderer('homepage')

@view_function
def process_request(request):
    
    params = {}
    print('>>>>>>>>>>>>>>>1')
    form = LoginForm()
    if request.method == 'POST':
        print('>>>>>>>>>>>>>>>0')
        form = LoginForm(request.POST)
        if form.is_valid():
            
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)

            return HttpResponse('''
                <script>
                $('#jquery-loadmodal-js').modal(hide):
                    window.location.href = '/homepage/index/';
                </script>
                ''')
            

    # do some edit work here
    params['form'] = form
    return templater.render_to_response(request, 'login.html' ,params)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label="Password",widget=forms.PasswordInput)

    def clean(self):
        try:
            print('>>>>>>>>>>>>> The beginning')
            username1 = self.cleaned_data['username']
            password1 = self.cleaned_data['password']

            s = Server('www.colonial-heritage.com', port=8389, get_info=GET_ALL_INFO)
            print('>>>>>>>>>>>> Connect Baby!!')
            print('>>>>>>>>>>>>>>>', s)
            c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC, user=username1 + '@colonial-heritage.local',password=password1,
            authentication=AUTH_SIMPLE, raise_exceptions=False)
            print('>>>>>>>>>>', c.password)
            print('<<<', (c.user))
            try:
                u = hmod.User.objects.get(username=username1)
                print('>>>>>>>>>>>>>>>Got user')
            except hmod.User.DoesNotExist:
                print('>>>>>>>>>>>>>create user')
                u = hmod.User()
                print('>>>>>>>>>>>>>created user')
                u.username = username1
                print('>>>>>>>>>>>>>', username1)
                u.set_password(password1)
                print('>>>>>>>>>>>>>', password1)
                u.first_name = "firstname"
                u.last_name = "lastname"
                u.email = "example@gmail.com"
                print('>>>>>>>>>>>>',u.email)
                u.save()
                print('>>>>>>>>>>>>>>>>>>saved')   
            
            user = authenticate(username=self.cleaned_data['username'],password=self.cleaned_data['password'])
            if user == None:
                raise forms.ValidationError('Username or password does not exist')
                return self.cleaned_data
            
        except:
            user = authenticate(username=self.cleaned_data['username'],password=self.cleaned_data['password'])
            if user == None:
                raise forms.ValidationError('Username or password does not exist')
                return self.cleaned_data
        


###########################################################################
################### logout
@view_function
def logout_view(request):
    logout(request)

    return HttpResponseRedirect('homepage/index/')

@view_function
def post_form(request):
    
    params = {}

    

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)

            return HttpResponse('''
                <script>
                    $('#jquery-loadmodal-js').modal('hide');
                    window.location.href = window.location.href;
                </script>
                ''')
            
    params['form'] = form
    return templater.render_to_response(request, 'loginform.html' ,params)
