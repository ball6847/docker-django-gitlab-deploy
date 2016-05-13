from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from tasks import deploy

class Project(models.Model):
    name = models.CharField(max_length=255, blank=False, help_text="Name of project (just for reminding purpose).")
    repo = models.CharField(max_length=255, blank=False, help_text="SSH URL of the repository (eg. git@git.bizidea.co.th:Bizidea/bizidea-mailer.git)")
    branch = models.CharField(max_length=255, blank=False, default="master", help_text="Source branch to pull from (default is master)")
    path = models.CharField(max_length=255, blank=False, help_text="Absolute path on server to clone repo into.")

    def __unicode__(self):
        return self.name

@receiver(post_save, sender=Project, dispatch_uid="notify_worker")
def notify_worker(sender, instance, **kwargs):
    deploy.delay(model_to_dict(instance))
