from django.db import models
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django_resized import ResizedImageField

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Review(models.Model):
    CURRENT = 'Current'
    FORMER = 'Former'

    RELATIONSHIP_CHOICES = (
        (CURRENT, 'Current'),
        (FORMER, 'Former'),
    )
    relationship = models.CharField(choices=RELATIONSHIP_CHOICES,
                                    default=CURRENT, max_length=50)
    content = models.TextField()
    last_interaction = models.DateField(blank=True, null=True)
    author = models.ForeignKey(get_user_model(), null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)

class AnalystReview(Review):
    CD = 'Consulting Days'
    SD = 'Strategy Development'
    MP = 'Market Positioning'
    RH = 'Research'
    WP = 'White Papers'

    STRENGTH_CHOICES = (
        (CD, CD),
        (SD, SD),
        (MP, MP),
        (RH, RH),
        (WP, WP),
    )

    SCORE_CHOICES = zip( range(1,6), range(1,6) )
    best_strength = models.CharField(choices=STRENGTH_CHOICES, max_length=50, null=True, blank=True)
    overall_rating = models.IntegerField(choices=SCORE_CHOICES, null=True)
    analyst = models.ForeignKey('Analyst', related_name='reviews_set')
    is_anonymous = models.BooleanField()

    def __unicode__(self):
        return str(self.author) + ' reviewed ' + str(self.analyst)

class HelpfulRating(models.Model):
    review = models.ForeignKey(Review)
    user = models.ForeignKey(get_user_model())
    upvote = models.BooleanField()

#set amount of base questions to be referenced
class AnalystRatingText(models.Model):
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text

#this is what gets created for reviews
class AnalystRating(models.Model):
    review = models.ForeignKey(AnalystReview)
    text = models.ForeignKey(AnalystRatingText)
    SCORE_CHOICES = zip( range(1,6), range(1,6) )
    rating = models.IntegerField(choices=SCORE_CHOICES)

class Analyst(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    analyst_firm = models.ForeignKey('AnalystFirm', related_name='analysts')
    years_experience = models.IntegerField(default=1)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(default=0, null=True)
    specializations = models.ManyToManyField('Specialization', blank=True)
    best_strength = models.CharField(choices=AnalystReview.STRENGTH_CHOICES, max_length=50, blank=True)
    recent_review = models.ForeignKey('AnalystReview', null=True, blank=True, related_name='+')
    photo = ResizedImageField(max_width=1024, max_length=1024, upload_to='analyst_images/', blank=True, null=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("ucapp.views.analyst_details", args=[str(self.id)])

class AnalystFirm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(default=0, null=True)
    photo = ResizedImageField(max_width=1024, max_length=1024, upload_to='analyst_firm_images/', blank=True, null=True)

    def __unicode__(self):
        return self.name