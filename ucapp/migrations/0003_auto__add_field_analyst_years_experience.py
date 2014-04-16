# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Analyst.years_experience'
        db.add_column(u'ucapp_analyst', 'years_experience',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Analyst.years_experience'
        db.delete_column(u'ucapp_analyst', 'years_experience')


    models = {
        u'ucapp.analyst': {
            'Meta': {'object_name': 'Analyst'},
            'analyst_firm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.AnalystFirm']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'years_experience': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'ucapp.analystfirm': {
            'Meta': {'object_name': 'AnalystFirm'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ucapp.analystrating': {
            'Meta': {'object_name': 'AnalystRating', '_ormbases': [u'ucapp.Rating']},
            u'rating_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ucapp.Rating']", 'unique': 'True', 'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.AnalystReview']"})
        },
        u'ucapp.analystreview': {
            'Meta': {'object_name': 'AnalystReview', '_ormbases': [u'ucapp.Review']},
            'analyst': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.Analyst']"}),
            u'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ucapp.Review']", 'unique': 'True', 'primary_key': 'True'}),
            'strength1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength5': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ucapp.rating': {
            'Meta': {'object_name': 'Rating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stars': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'ucapp.review': {
            'Meta': {'object_name': 'Review'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_interaction': ('django.db.models.fields.DateField', [], {}),
            'relationship': ('django.db.models.fields.CharField', [], {'default': "'Current'", 'max_length': '50'})
        }
    }

    complete_apps = ['ucapp']