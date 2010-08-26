from django.conf.urls.defaults import *
from chameleon.reader.views import *
from chameleon.reader.models import *
import os.path

from django.views.generic import list_detail
from django.contrib import admin
from django.views.generic.simple import direct_to_template
site_media = os.path.join( os.path.dirname(__file__), 'media' )

admin.autodiscover()

urlpatterns = patterns('',

    #(r'^admin/', include(admin.site.urls)),
    (r'^admin/(.*)', admin.site.root),

    # Browsing
    url(r'^$', index, name='index_view'),
    
    url(r'^opensearch.xml$', direct_to_template,
            { 'template': 'osd/opensearch.xml',
              'mimetype': 'application/opensearchdescription+xml' },
              name="opensearch"),
    
    # social network
    url(r'^friends/(\w+)/', friends , name="friends"),
    # (r'^friend/add/$', friend_add),
    url(r'^friend/invite/$', friend_invite, name="invite"),
    # (r'^friend/accept/(\w+)/$', friend_accept),
	
	#(r'feedjack/(.*)', include('feedjack.urls')),
    
    #(r'^accounts/', include('registration.urls')),
    #user management
    url(r'^accounts/create/', create_account , name="create"),
    url(r'^accounts/logout/', logout_view, name="logout" ),
    url(r'^accounts/login/', 'django.contrib.auth.views.login' , name="login" ),
    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    (r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    
    
    # reader urls
    (r'^reader/', include('chameleon.reader.urls') ),

    
    #Site media - manage static content
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
	
)
