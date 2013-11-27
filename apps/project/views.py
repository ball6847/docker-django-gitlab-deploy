import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from unipath import Path
from .utils import shell_exec, su, get_closest_uid, get_name_from_uid
import sys, os

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
	
	uid = get_closest_uid(path)
	user = get_name_from_uid(uid)
	
	#os.setgid(uid)
	#os.seteuid(uid)
	
	if path.isfile():
		return HttpResponse("Expected deploy path to be a directory");
	elif not path.isdir():
		try:
			path.mkdir(True)
		except:
			return HttpResponse("Cannot create target directory");
	
	path.chdir()
	
	if not path.child('.git').isdir():
		print shell_exec(['su', user, '-c', 'git init'])
		print shell_exec(['su', user, '-c', 'git remote add origin ' + repo['url']])
	
	# run in background
	shell_exec([sys.executable, settings.PROJECT_ROOT.child('manage.py'), 'updaterepo', project_id], False)
	
	return HttpResponse("Message recieved");
