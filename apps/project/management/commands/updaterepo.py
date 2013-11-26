from django.core.management.base import BaseCommand, CommandError
from project.models import Project
from project.utils import shell_exec, get_closest_uid, get_name_from_uid, su
import os

class Command(BaseCommand):
	def handle(self, *args, **options):
		for project_id in args:
			try:
				project = Project.objects.get(pk=project_id)
			except:
				continue
				
			os.chdir(project.path)
			
			shell_exec(['git', 'fetch', '-f', 'origin', 'master'])
			shell_exec(['git', 'reset', '--hard', 'FETCH_HEAD'])
