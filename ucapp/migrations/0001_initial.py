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
            ('analyst_firm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='analysts', to=orm['ucapp.AnalystFirm'])),
            ('years_experience', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'ucapp', ['Analyst'])

        # Adding model 'Review'
        db.create_table(u'ucapp_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relationship', self.gf('django.db.models.fields.CharField')(default='Current', max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('last_interaction', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
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
            ('best_strength', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('overall_rating', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('analyst', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ucapp.Analyst'])),
            ('is_anonymous', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ucapp', ['AnalystReview'])

        # Adding model 'HelpfulRating'
        db.create_table(u'ucapp_helpfulrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ucapp.Review'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('upvote', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'ucapp', ['HelpfulRating'])

        # Adding model 'AnalystRatingText'
        db.create_table(u'ucapp_analystratingtext', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ucapp', ['AnalystRatingText'])

        # Adding model 'Rating'
        db.create_table(u'ucapp_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stars', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ucapp', ['Rating'])

        # Adding model 'AnalystRating'
        db.create_table(u'ucapp_analystrating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ucapp.AnalystReview'])),
            ('text', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ucapp.AnalystRatingText'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
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

        # Deleting model 'HelpfulRating'
        db.delete_table(u'ucapp_helpfulrating')

        # Deleting model 'AnalystRatingText'
        db.delete_table(u'ucapp_analystratingtext')

        # Deleting model 'Rating'
        db.delete_table(u'ucapp_rating')

        # Deleting model 'AnalystRating'
        db.delete_table(u'ucapp_analystrating')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ucapp.analyst': {
            'Meta': {'object_name': 'Analyst'},
            'analyst_firm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'analysts'", 'to': u"orm['ucapp.AnalystFirm']"}),
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
            'Meta': {'object_name': 'AnalystRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.AnalystReview']"}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.AnalystRatingText']"})
        },
        u'ucapp.analystratingtext': {
            'Meta': {'object_name': 'AnalystRatingText'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'ucapp.analystreview': {
            'Meta': {'object_name': 'AnalystReview', '_ormbases': [u'ucapp.Review']},
            'analyst': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.Analyst']"}),
            'best_strength': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'is_anonymous': ('django.db.models.fields.BooleanField', [], {}),
            'overall_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'review_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ucapp.Review']", 'unique': 'True', 'primary_key': 'True'}),
            'strength1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength5': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ucapp.helpfulrating': {
            'Meta': {'object_name': 'HelpfulRating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ucapp.Review']"}),
            'upvote': ('django.db.models.fields.BooleanField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ucapp.rating': {
            'Meta': {'object_name': 'Rating'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stars': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ucapp.review': {
            'Meta': {'object_name': 'Review'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_interaction': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'default': "'Current'", 'max_length': '50'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ucapp']