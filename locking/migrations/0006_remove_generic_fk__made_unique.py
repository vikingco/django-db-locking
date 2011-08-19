# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'Lock', fields ['object_id', 'content_type']
        db.delete_unique('locking_lock', ['object_id', 'content_type_id'])

        # Deleting field 'Lock.object_id'
        db.delete_column('locking_lock', 'object_id')

        # Deleting field 'Lock.content_type'
        db.delete_column('locking_lock', 'content_type_id')

        # Adding unique constraint on 'Lock', fields ['locked_object']
        db.create_unique('locking_lock', ['locked_object'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Lock', fields ['locked_object']
        db.delete_unique('locking_lock', ['locked_object'])

        # Adding field 'Lock.object_id'
        db.add_column('locking_lock', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)

        # We cannot add back in field 'Lock.content_type'
        raise RuntimeError(
            "Cannot reverse this migration. 'Lock.content_type' and its values cannot be restored.")

        # Adding unique constraint on 'Lock', fields ['object_id', 'content_type']
        db.create_unique('locking_lock', ['object_id', 'content_type_id'])


    models = {
        'locking.lock': {
            'Meta': {'ordering': "['created_on']", 'object_name': 'Lock'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locked_object': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'max_age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3600'})
        }
    }

    complete_apps = ['locking']
