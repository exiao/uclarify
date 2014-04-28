from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.default.views import RegistrationView
from ucapp.forms import NewEmailRegistrationForm
from django.conf.urls.static import static
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ucapp.views.home', name='home'),
    url(r'^analyst/$', 'ucapp.views.analyst', name='analyst'),
    url(r'^analyst/(?P<analyst_id>\d+)/$', 'ucapp.views.analyst_details', name='analyst_details'),
    url(r'^analyst/(?P<analyst_id>\d+)/write/$', 'ucapp.views.review_analyst', name='review_analyst'),
    url(r'^analyst-firm/$', 'ucapp.views.analyst_firm', name='analyst_firm'),
    url(r'^analyst-firm/(?P<analyst_firm_id>\d+)/$', 'ucapp.views.analyst_firm_details', name='analyst_firm_details'),
    url(r'^pr-agency/$', 'ucapp.views.pr_agency', name='pr_agency'),
    url(r'^search/$', 'ucapp.views.search', name='search'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/', include('haystack.urls')),
    url(r'^ajax/search/$', 'ucapp.views.ajax_search', name='ajax_search'),

    ##### REGISTRATION CODE #####
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r"^complete/", "li_registration.views.complete", name="complete"),
    url(r"^logout/", "li_registration.views.logout", name="logout"),
    url(r"^register/$",
        RegistrationView.as_view(form_class=NewEmailRegistrationForm),
        name="registration_register",
    ),
    url(r'^account/$', 'li_registration.views.account_profile', name='account_profile'),
    url(r'', include("registration_email.backends.default.urls")),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
