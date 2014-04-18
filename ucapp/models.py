from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class AnalystFirm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __unicode__(self):
        return self.name

class Analyst(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    analyst_firm = models.ForeignKey(AnalystFirm, related_name='analysts')
    years_experience = models.IntegerField(default=1)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.full_name

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

    strength1 = models.CharField(choices=STRENGTH_CHOICES, max_length=50)
    strength2 = models.CharField(choices=STRENGTH_CHOICES, max_length=50)
    strength3 = models.CharField(choices=STRENGTH_CHOICES, max_length=50)
    strength4 = models.CharField(choices=STRENGTH_CHOICES, max_length=50)
    strength5 = models.CharField(choices=STRENGTH_CHOICES, max_length=50)
    analyst = models.ForeignKey(Analyst)

    def __unicode__(self):
        return str(self.author) + ' ' + str(self.analyst)

class HelpfulRating(models.Model):
    review = models.ForeignKey(Review)
    user = models.ForeignKey(get_user_model())
    upvote = models.BooleanField()

class Rating(models.Model):
    SCORE_CHOICES = zip( range(1,6), range(1,6) )
    stars = models.IntegerField(choices=SCORE_CHOICES)
    text = models.CharField(max_length=200)

class AnalystRating(Rating):
    review = models.ForeignKey(AnalystReview)
