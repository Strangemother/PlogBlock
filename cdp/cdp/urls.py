from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from views import Index, LogFileList, ParseView, CsvView
import os
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view(), name='cdp_index'),
    url(r'^files/$', LogFileList.as_view(), name='cdp_files'),
    url(r'^parse/(?P<file>.*)/$', ParseView.as_view(), name='cdp_parse'),
    url(r'^parse/$', ParseView.as_view(), name='cdp_parse'),
    url(r'^csv/(?P<parse>.*)/save/$', CsvView.as_view(), name='cdp_csv'),
    url(r'^csv/(?P<parse>.*)/$', CsvView.as_view(), name='cdp_csv'),
    # url(r'^cdp/', include('cdp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# Media urls
urlpatterns += patterns('',             
  (r'^media/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
  (r'^static/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
  (r'^st/(?P<path>.*)$', 'django.views.static.serve',
      {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
)
