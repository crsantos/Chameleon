from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.template import loader, Context

from django.template import RequestContext

def index(request):

    return render_to_response('reader/index.html',
        {
            'title': "Chameleon"
            
        },context_instance=RequestContext(request))