from django.contrib import admin
from .models import Project
from django.core.urlresolvers import reverse

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'repo', 'path', 'callback_url')
    search_fields = ('name', 'repo', 'path')

    def get_queryset(self, request):
        """
        Just to hook for HttpRequest object, use later in self.callback_url
        But also, we can use this method to filter result for each user
        see https://docs.djangoproject.com/en/1.9/ref/contrib/admin/#django.contrib.admin.ModelAdmin.get_queryset
        """
        self._request = request
        return super(ProjectAdmin, self).get_queryset(request)

    def callback_url(self, obj):
    	uri = reverse('project.deploy', args=[obj.pk])
    	return '<a href="%s">%s</a>' % (uri, self._request.build_absolute_uri(uri))


    callback_url.allow_tags = True
    callback_url.short_description = 'Callback url'

admin.site.register(Project, ProjectAdmin)
