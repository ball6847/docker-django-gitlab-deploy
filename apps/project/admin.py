from django.contrib import admin
from .models import Project
from django.core.urlresolvers import reverse

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'repo', 'path', 'callback_url')
	search_fields = ('name', 'repo', 'path')

	def callback_url(self, obj):
		uri = reverse('project.deploy', args=[obj.pk])
		return '<a href="%s">%s</a>' % (uri, uri)

	callback_url.allow_tags = True
	callback_url.short_description = 'Callback url'

admin.site.register(Project, ProjectAdmin)
