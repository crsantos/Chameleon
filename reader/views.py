from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader, Context, RequestContext
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from reader.views import *
from chameleon.reader.models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import password_reset
from django.contrib.auth.forms  import PasswordResetForm
from django.contrib.auth.tokens  import default_token_generator
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
@login_required
def source(request,slug):
    return render_to_response('reader/source.html',
        {
            'title': "Chameleon search",
            'source': Source.objects.get(slug=slug)

        },context_instance=RequestContext(request))

######################################################################

@login_required
def tag(request,slug):
    return render_to_response('reader/tag.html',
        {
            'title': "Chameleon tags",
            'tag': Tag.objects.get(slug=slug)

        },context_instance=RequestContext(request))

######################################################################

@login_required
def article(request,slug):
    return render_to_response('reader/article.html',
        {
            'title': "Chameleon articles",
            'article': Article.objects.get(slug=slug)

        },context_instance=RequestContext(request))

######################################################################


def create_account(request):
    
    if request.method=="POST":
        return HttpResponse("post")
    else:
        return HttpResponse("get")
        
######################################################################

def logout_view(request):
    logout(request)
    return HttpResponseRedirect( reverse("index_view") )
    
######################################################################

