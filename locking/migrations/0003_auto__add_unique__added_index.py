# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding index on 'Lock', fields ['created_on']
        db.create_index('locking_lock', ['created_on'])

        # Adding unique constraint on 'Lock', fields ['object_id', 'content_type']
        db.create_unique('locking_lock', ['object_id', 'content_type_id'])


    def backwards(self, orm):
        
        # Removing index on 'Lock', fields ['created_on']
        db.delete_index('locking_lock', ['created_on'])

        # Removing unique constraint on 'Lock', fields ['object_id', 'content_type']
        db.delete_unique('locking_lock', ['object_id', 'content_type_id'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'locking.lock': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'Lock'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3600'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['locking']
