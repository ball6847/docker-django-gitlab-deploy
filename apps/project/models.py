from django.db import models
from django.conf import settings
from unipath import Path

class Project(models.Model):
	name = models.CharField(max_length=255, blank=False)

	path = models.CharField(max_length=255,
							blank=False,)
	
	def __unicode__(self):
		return self.name
