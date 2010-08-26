from django.conf.urls.defaults import *
from chameleon.reader.models import *
from chameleon.reader.views import *
from django.views.generic import list_detail

source_list = {
    "queryset" : Source.objects.order_by('name'),
    "extra_context" : {'title': "Sources", 'tags': tag_cloud()},
    "paginate_by": 1,
    'template_object_name': 'source'
}
tag_list = {
    "queryset" : Tag.objects.order_by('name'),
    "extra_context" : {'title': "Tags", 'tags': tag_cloud()},
    "paginate_by": 1,
    'template_object_name': 'tag'
}
article_list = {
    "queryset" : Article.objects.order_by('name'),
    "extra_context" : {'title': "Articles", 'tags': tag_cloud()},
    "paginate_by": 1,
    'template_object_name': 'article'
}

urlpatterns = patterns('',

    # Browsing
    url(r'^$', index, name="reader_index"),
    url(r'^sources/$', list_detail.object_list, source_list, name="sources"),
    url(r'^source/(?P<slug>[-\w]+)/$', source, name="source"),
    url(r'^sources/add/$', add_source, name="add_source"),
    
    
    url(r'^tags/$', list_detail.object_list, tag_list, name="tags"),
	url(r'^tag/(?P<slug>[-\w]+)/$', tag, name="tag"),
    # url(r'^tagcloud/$', tag_cloud_page, name="tagcloud"),
    
	
	url(r'^articles/$', list_detail.object_list, article_list, name="articles"),
	url(r'^article/(?P<slug>[-\w]+)/$', article, name="article"),
    
)
