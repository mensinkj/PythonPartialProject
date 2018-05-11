from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from homepage import models as hmod
from django.http import HttpResponse, HttpResponseRedirect, Http404

templater = get_renderer('homepage')
@view_function
def process_request(request):


	return templater.render_to_response(request,'index.html')