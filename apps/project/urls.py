from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url("^([^/]+)/?$", 'project.views.deploy', name='project.deploy'),
)
