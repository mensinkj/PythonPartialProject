from django.conf import settings
from django_mako_plus.controller import view_function
from django_mako_plus.controller.router import get_renderer
from homepage import models as hmod
from django.http import HttpResponse, HttpResponseRedirect, Http404


templater = get_renderer('homepage')

@view_function
def process_request(request):
#	params = prepare_params(request)

	return templater.render_to_response(request,'index.html')

@view_function
def batch(request):

	params = {}

	try:
		print('>>>>>>>>>>>> 1')
		all_rentals = hmod.Rentals.objects.all().order_by('days_late')
	except hmod.Rentals.DoesNotExist:
		print('Database contains no rentals')
		#return HttpResponseRedirect('homepage/database_err')
	print('>>>>>>>>>>>2')
	params['all_rentals'] = all_rentals
	print('>>>>>>>>>>>>>>>>>3')
	return templater.render_to_response(request, 'batch.html' ,params)



