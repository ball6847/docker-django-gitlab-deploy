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

	path = Path(project.path)
	params = json.loads(request.body)
	repo = params['repository']
	
	if path.isfile():
		return HttpResponse("Expected deploy path to be a directory");
	elif not path.isdir():
		# path.mkdir(True) need exception
		try:
			path.mkdir(True)
		except:
			return HttpResponse("Cannot create target directory");
	
	path.chdir()
	
	if not path.child('.git').isdir():
		print shell_exec(['git', 'init'])
		print shell_exec(['git', 'remote', 'add', 'origin', repo['url']])
	
	# run in background
	shell_exec(['/bin/sh', settings.PROJECT_ROOT.child('bin', 'working_copy_update.sh')], False)
	
	return HttpResponse("Message recieved");
