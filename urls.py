from django.conf.urls.defaults import *
from chameleon.reader.models import *
from reader.views import *
import os.path
from django.views.generic import list_detail
from django.contrib import admin
from django.views.generic.simple import direct_to_template
site_media = os.path.join( os.path.dirname(__file__), 'media' )

admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),

    
    # Browsing
    url(r'^$', index, name='index_view'),
    url(r'^opensearch.xml$', direct_to_template,
            { 'template': 'osd/opensearch.xml',
              'mimetype': 'application/opensearchdescription+xml' },
              name="opensearch"),
    (r'^search/', search ),
    
    # reader urls
    (r'^reader/', include('chameleon.reader.urls') ),
    

    
    #Site media - manage static content
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
	
)
