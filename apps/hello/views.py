from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return HttpResponse(reverse('hello.index'));

def eiei(request):
	return HttpResponse('From eiei');