from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ucapp.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^analyst/$', 'analyst', name='analyst'),
    # url(r'^analyst/(?P<analyst_id>\d+)/$', 'analyst_details', name='analyst_details'),
    url(r'^analyst-firm/$', 'analyst_firm', name='analyst_firm'),
    url(r'^pr-agency/$', 'pr_agency', name='pr_agency'),
    url(r'^search/$', 'search', name='search'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^search/', include('haystack.urls')),
    url(r'^ajax/search/$', 'ajax_search', name='ajax_search'),
    url(r'^trash/write$', 'write')
)
