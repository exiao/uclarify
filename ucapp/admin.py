from django.contrib import admin
from models import Analyst, AnalystFirm, AnalystReview, AnalystRating

# Register your models here.

admin.site.register(AnalystReview)
admin.site.register(Analyst)
admin.site.register(AnalystFirm)
admin.site.register(AnalystRating)