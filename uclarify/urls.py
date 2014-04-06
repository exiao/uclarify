from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ucapp.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^analyst/', 'analyst', name='analyst'),
    url(r'^search/', 'search', name='search'),

    url(r'^admin/', include(admin.site.urls)),
)
