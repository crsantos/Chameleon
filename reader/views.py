from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader, Context, RequestContext
from reader.views import *
from chameleon.reader.models import *

######################################################################

def index(request):

    return render_to_response('reader/index.html',
        {
            'title': "Chameleon"

        },context_instance=RequestContext(request))

######################################################################        

def search(request):
    
    q= request.GET.get('q','')
    if q != '':
        return render_to_response('search/search.html',
            {
                'title': "Chameleon search",
                'search': Source.objects.filter(name__icontains=q),
            },context_instance=RequestContext(request))
    else:
        return render_to_response('search/search.html',
            {
                'title': "Chameleon search",
            },context_instance=RequestContext(request))
            
######################################################################

def source(request,slug):
    return render_to_response('reader/source.html',
        {
            'title': "Chameleon search",
            'source': Source.objects.get(slug=slug)

        },context_instance=RequestContext(request))

######################################################################