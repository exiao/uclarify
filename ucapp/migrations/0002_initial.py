# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AnalystFirm'
        db.create_table(u'ucapp_analystfirm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ucapp', ['AnalystFirm'])

        # Adding model 'Analyst'
        db.create_table(u'ucapp_analyst', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('analyst_firm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ucapp.AnalystFirm'])),
        ))
        db.send_create_signal(u'ucapp', ['Analyst'])

        # Adding model 'Review'
        db.create_table(u'ucapp_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(default='Current', max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('last_interaction', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ucapp', ['Review'])

        # Adding model 'AnalystReview'
        db.create_table(u'ucapp_analystreview', (
            (u'review_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ucapp.Review'], unique=True, primary_key=True)),
            ('strength1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('strength2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('strength3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('strength4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('strength5', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('analyst', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ucapp.Analyst'])),
        ))
        db.send_create_signal(u'ucapp', ['AnalystReview'])

        # Adding model 'Rating'
        db.create_table(u'ucapp_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stars', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ucapp', ['Rating'])

        # Adding model 'AnalystRating'
        db.create_table(u'ucapp_analystrating', (
            (u'rating_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ucapp.Rating'], unique=True, primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ucapp.AnalystReview'])),
        ))
        db.send_create_signal(u'ucapp', ['AnalystRating'])


    def backwards(self, orm):
        # Deleting model 'AnalystFirm'
        db.delete_table(u'ucapp_analystfirm')

        # Deleting model 'Analyst'
        db.delete_table(u'ucapp_analyst')

        # Deleting model 'Review'
        db.delete_table(u'ucapp_review')

        # Deleting model 'AnalystReview'
        db.delete_table(u'ucapp_analystreview')

        # Deleting model 'Rating'
        db.delete_table(u'ucapp_rating')

        # Deleting model 'AnalystRating'
        db.delete_table(u'ucapp_analystrating')


    models = {
        u'ucapp.analyst': {
            'Meta': {'object_name': 'Analyst'},
            'analyst_firm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.AnalystFirm']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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