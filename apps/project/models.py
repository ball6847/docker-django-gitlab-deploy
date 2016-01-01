from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from tasks import deploy

class Project(models.Model):
	name = models.CharField(max_length=255, blank=False)
	repo = models.CharField(max_length=255,
							blank=False,)
	path = models.CharField(max_length=255,
							blank=False,)

	def __unicode__(self):
		return self.name

@receiver(post_save, sender=Project, dispatch_uid="notify_worker")
def notify_worker(sender, instance, **kwargs):
    deploy.delay(model_to_dict(instance))
