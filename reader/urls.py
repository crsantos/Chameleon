from django.conf.urls.defaults import *
from chameleon.reader.models import *
from reader.views import *
from django.views.generic import list_detail

source_list = {
    "queryset" : Source.objects.order_by('name'),
    "extra_context" : {'title': "Sources"},
    "paginate_by": 1,
    'template_object_name': 'source'
}

urlpatterns = patterns('',

    # Browsing
    url(r'^$', index, name="reader_index"),
    url(r'^sources/$', list_detail.object_list, source_list, name="cenas"),
    
    url(r'^source/(?P<slug>[-\w]+)/$', source, name="cenas"),
	
)