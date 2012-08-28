# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Talk'
        db.create_table('submission_talk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('macro_theme', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('type', self.gf('django.db.models.fields.CharField')(default='talk', max_length=20)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('submission', ['Talk'])


    def backwards(self, orm):
        # Deleting model 'Talk'
        db.delete_table('submission_talk')


    models = {
        'submission.talk': {
            'Meta': {'object_name': 'Talk'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'macro_theme': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '14'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'talk'", 'max_length': '20'})
        }
    }

    complete_apps = ['submission']