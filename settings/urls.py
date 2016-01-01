from django.conf.urls import include, url
from home import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r"^project/", include('project.urls')),
	url(r'^', views.index, name='home'),
]
