# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Project.user'
        db.delete_column(u'project_project', 'user')


    def backwards(self, orm):
        # Adding field 'Project.user'
        db.add_column(u'project_project', 'user',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    models = {
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['project']