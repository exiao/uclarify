from django.db import models

# Create your models here.
class AnalystFirm(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Analyst(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    analyst_firm = models.ForeignKey(AnalystFirm)

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
    last_interaction = models.DateField()

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

class Rating(models.Model):
    SCORE_CHOICES = zip( range(1,6), range(1,6) )
    stars = models.IntegerField(choices=SCORE_CHOICES, blank=True)
    text = models.CharField(max_length=200)

class AnalystRating(Rating):
    review = models.ForeignKey(AnalystReview)
