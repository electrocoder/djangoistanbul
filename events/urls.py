from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'events.views.index'),
)

