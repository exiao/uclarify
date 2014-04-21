from django.contrib import admin
from models import Analyst, AnalystFirm, AnalystReview, AnalystRating, AnalystRatingText, Specialization

# Register your models here.

admin.site.register(AnalystReview)
admin.site.register(Analyst)
admin.site.register(AnalystFirm)
admin.site.register(AnalystRating)
admin.site.register(AnalystRatingText)
admin.site.register(Specialization)
