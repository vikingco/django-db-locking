
from south.db import db
from django.db import models
from locking.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Lock'
        db.create_table('locking_lock', (
            ('id', orm['locking.Lock:id']),
            ('content_type', orm['locking.Lock:content_type']),
            ('object_id', orm['locking.Lock:object_id']),
            ('created_on', orm['locking.Lock:created_on']),
        ))
        db.send_create_signal('locking', ['Lock'])
        
        # Creating unique_together for [content_type, object_id] on Lock.
        db.create_unique('locking_lock', ['content_type_id', 'object_id'])
        
    
    
    def backwards(self, orm):
        
        # Deleting unique_together for [content_type, object_id] on Lock.
        db.delete_unique('locking_lock', ['content_type_id', 'object_id'])
        
        # Deleting model 'Lock'
        db.delete_table('locking_lock')
        
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'locking.lock': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }
    
    complete_apps = ['locking']
