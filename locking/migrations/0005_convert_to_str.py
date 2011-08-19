# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for l in orm.Lock.objects.all():
            ct = ContentType.objects.get(app_label=l.content_type.app_label, model=l.content_type.model)
            model = ct.model_class
            l.locked_object = '%s.%s__%d' % (model.__module__, model.__name__, l.object_id)
            l.save()


    def backwards(self, orm):
        "Write your backwards methods here."
        pass


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'locking.lock': {
            'Meta': {'ordering': "['created_on']", 'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'Lock'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locked_object': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'max_age': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3600'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['locking']
