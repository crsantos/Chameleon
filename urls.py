from django.conf.urls.defaults import *
from chameleon.reader.models import *
from reader.views import *
import os.path
from django.views.generic import list_detail
from django.contrib import admin
site_media = os.path.join( os.path.dirname(__file__), 'media' )

admin.autodiscover()

source_list = {
    "queryset" : Source.objects.order_by('name'),
    "extra_context" : {'title': "Sources"},
    "paginate_by": 1,
    'template_object_name': 'source'
}

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    
    # Browsing
	url(r'^$', index, name='index_view'),
    (r'^sources/$', list_detail.object_list, source_list),
    
    #Site media - manage static content
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
	
)
