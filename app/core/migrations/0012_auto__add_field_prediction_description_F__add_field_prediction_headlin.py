# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Prediction.description_F'
        db.add_column(u'core_prediction', 'description_F',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=300, blank=True),
                      keep_default=False)

        # Adding field 'Prediction.headline_F'
        db.add_column(u'core_prediction', 'headline_F',
                      self.gf('django.db.models.fields.TextField')(default='', max_length=300, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Prediction.description_F'
        db.delete_column(u'core_prediction', 'description_F')

        # Deleting field 'Prediction.headline_F'
        db.delete_column(u'core_prediction', 'headline_F')


    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title_D': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'title_E': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'title_F': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'core.prediction': {
            'Meta': {'object_name': 'Prediction'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Category']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_D': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'description_E': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'description_F': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'edition_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'editors_pick': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'headline_D': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'headline_E': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'headline_F': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_credit': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'more_info': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Source']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'year_predicted': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        },
        u'core.realisation': {
            'Meta': {'object_name': 'Realisation'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description_D': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'description_E': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'edition_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_credit': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'more_info': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'prediction': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'realisations'", 'to': u"orm['core.Prediction']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'year_introduced': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.source': {
            'Meta': {'object_name': 'Source'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'description_D': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'description_E': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'description_F': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'image_credit': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'more_info': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'series_episode': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'series_season': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title_D': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'title_E': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'title_F': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'year_published': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']