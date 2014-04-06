from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ucapp.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^analyst/$', 'analyst', name='analyst'),
    url(r'^analyst/', 'analyst', name='analyst'),
    url(r'^analyst-firm/$', 'analystFirm', name='analystFirm'),
    url(r'^pr-agency/$', 'prAgency', name='prAgency'),
    url(r'^admin/', include(admin.site.urls)),
)
