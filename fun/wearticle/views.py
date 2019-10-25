from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views import View
from django.utils.decorators import method_decorator


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

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super( HelloView, self ).dispatch( request, *args, **kwargs )
