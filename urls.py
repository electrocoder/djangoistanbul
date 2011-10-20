from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'djangoistanbul.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
