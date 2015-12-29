from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from unipath import Path
from models import Project
from django.forms.models import model_to_dict
import tasks

@csrf_exempt
def deploy(request, project_id):
    """
    Deploy project to specific location
    """
    try:
    	project = Project.objects.get(pk=project_id)
    except:
    	return HttpResponse("Project not found");

    path = Path(project.path)

    if path.isfile():
    	return HttpResponse("Expected deploy path to be a directory");

    # add tasks to messagequeue server
    tasks.deploy.delay(model_to_dict(project))

    return HttpResponse("Task dispatched, your project should be deployed shortly.");
