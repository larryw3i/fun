from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views import View
from django.utils.decorators import method_decorator
from django.urls.converters import IntConverter
from django.views.generic import TemplateView
from .apps import AppConfig





# @csrf_exampt
@require_http_methods( ['GET',] )
def hello_django_bbs( request ):
	html = '<h1>Hello Django BBS</h1>'
	return HttpResponse( html )

class HelloView( View ):
	html = '%s Hello Django BBS'

	def get(self, request):
		return HttpResponse( self.html % 'GET' )

	def post(self, request):
		return HttpResponse( self.html % 'POST' )

	def dynamic_hello(self, request, year, month, day = 15):
		html = '<h1> (%s) Hello Django BBS  </h1>'
		return HttpResponse( html % (' %s - %s - %s ') %  (year, month, day)  )
	
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super( HelloView, self ).dispatch( request, *args, **kwargs )
	
class MonthConverter( IntConverter ):
	regex = '0?[1-9]|1[0-2]'
		
