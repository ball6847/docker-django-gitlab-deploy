import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from unipath import Path
from .utils import shell_exec


from models import Project

try:
    import json
except ImportError:
    import simplejson as json

@csrf_exempt
def deploy(request, project_id):
	"""
	Deploy project to specific location
	"""
	
	try:
		project = Project.objects.get(pk=project_id)
	except:
		return HttpResponse("Project not found");

	if not request.body:
		return HttpResponse("Expected repository data");
	
	print request.body
	
	return HttpResponse("it should be ok");

	path = Path(project.path)
	params = json.loads(request.body)
	repo = params.repository
	
	print params.repository
	
	if path.isfile():
		return HttpResponse("Expected deploy path to be a directory");
	elif not path.isdir() and not path.mkdir(True):
		return HttpResponse("Cannot create deploy directory for target key");

	
	print "OK, it works"
	
	#path.chdir()
	#
	#if not path.child('.git').isdir():
	#	shell_exec(['git', 'init'])
	#	shell_exec(['git', 'remote', 'add', 'origin', repo.url])
	#
	#shell_exec(['git', 'clean', '-fdx'])
	#shell_exec(['git', 'fetch', '-f', 'origin', 'master'])
	#shell_exec(['git', 'reset', '--hard', 'FETCH_HEAD'])
	
	return HttpResponse("Message recieved");
