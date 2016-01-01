from django.conf.urls import url
from .views import deploy

urlpatterns = [
	url("^([^/]+)/?$", deploy, name='project.deploy'),
]
