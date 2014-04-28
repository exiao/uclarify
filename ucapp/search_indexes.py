from haystack import indexes
from models import Analyst, AnalystFirm
import datetime

class AnalystIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name', boost=1.5)
    last_name = indexes.CharField(model_attr='last_name', boost=1.5)
    analyst_firm = indexes.CharField(model_attr='analyst_firm')
    average_rating = indexes.DecimalField(model_attr='average_rating', null=True)
    num_reviews = indexes.IntegerField(model_attr='num_reviews', null=True)
    specializations = indexes.MultiValueField()

    def get_model(self):
        return Analyst

    def prepare_specializations(self, obj):
        return [specialization.pk for specialization in obj.specializations.all()]

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class AnalystFirmIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', boost=1.5)
    description = indexes.CharField(model_attr='description')
    average_rating = indexes.DecimalField(model_attr='average_rating', null=True)
    num_reviews = indexes.IntegerField(model_attr='num_reviews', null=True)

    def get_model(self):
        return AnalystFirm

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
