from django.conf.urls import patterns, include, url

urlpatterns = patterns('hello.views',
	url("^$", 'index', name='hello.index'),
	url("^eiei/$", 'eiei', name='hello.eiei'),
)
