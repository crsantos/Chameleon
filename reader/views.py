from chameleon.django.shortcuts import render_to_response, get_object_or_404
from chameleon.django.core.exceptions import ObjectDoesNotExist
from chameleon.django.http import HttpResponse, Http404, HttpResponseRedirect
from chameleon.django.core.urlresolvers import reverse
from chameleon.django.template import loader, Context, RequestContext
from chameleon.django.contrib.auth import logout
from chameleon.django.contrib.auth.forms import UserCreationForm
from reader.views import *
from reader.forms import *
from reader.models import *
from chameleon.django.contrib.auth.decorators import login_required, permission_required
from chameleon.django.contrib.auth.views import password_reset
from chameleon.django.contrib.auth.forms  import PasswordResetForm
from chameleon.django.contrib.auth.tokens  import default_token_generator
from chameleon.django.contrib import messages

######################################################################

def index(request):
    return render_to_response('reader/index.html',
        {
            'title': "Chameleon",
            'tags': tag_cloud()

        },context_instance=RequestContext(request))

######################################################################        

def search(request):
    
    q= request.GET.get('q','')
    if q != '':
        return render_to_response('search/search.html',
            {
                'title': "Chameleon search",
                'search': Source.objects.filter(name__icontains=q),
                'tags': tag_cloud()
                
            },context_instance=RequestContext(request))
    else:
        return render_to_response('search/search.html',
            {
                'title': "Chameleon search",
                'tags': tag_cloud()
            },context_instance=RequestContext(request))
            
######################################################################
@login_required
def source(request,slug):
    return render_to_response('reader/source.html',
        {
            'title': "Chameleon search",
            'source': Source.objects.get(slug=slug),
            'tags': tag_cloud()

        },context_instance=RequestContext(request))

######################################################################

@login_required
def tag(request,slug):
    tag = get_object_or_404(Tag, slug=slug) 
    articles = tag.articles.order_by('-id')
    return render_to_response('reader/tag.html',
        {
            'title': "Chameleon tags",
            'articles': articles,
            'tag': Tag.objects.get(slug=slug),
            'tags': tag_cloud()

        },context_instance=RequestContext(request))

######################################################################

@login_required
def article(request,slug):
    return render_to_response('reader/article.html',
        {
            'title': "Chameleon articles",
            'article': Article.objects.get(slug=slug),
            'tags': tag_cloud()

        },context_instance=RequestContext(request))

######################################################################


def create_account(request):
    
    if request.user.is_anonymous():    

        if request.method=="POST":
            form = UserCreationForm( request.POST )
            if form.is_valid():
                user = form.save()
            return HttpResponseRedirect(reverse('index_view'))
        else:
            form = UserCreationForm()
        return render_to_response('registration/register.html',
            {
                'title': "Register Account",
                'form': form,
                'tags': tag_cloud()
                
            },context_instance=RequestContext(request))

    else:
        messages.add_message(request, messages.INFO,"Already logged in...")
        return HttpResponseRedirect(reverse('index_view'))
    
######################################################################

def logout_view(request):
    logout(request)
    return HttpResponseRedirect( reverse("index_view") )
    
######################################################################

# FRIENDSHIPS

def friends(request, username):
	user = get_object_or_404(User, username=username) 
	friends = [friendship.to_friend for friendship in user.friend_set.all()] 
	#friend_playlists = Playlist.objects.filter(user__in=friends).order_by('-id') 
	variables = RequestContext(request, {
		'username': username, 
		'friends': friends,
		'tags': tag_cloud()
		#'playlists': friend_playlists[:10],
	})
	return render_to_response('friends/index.html', variables)

######################################################################

@login_required
def friend_add(request): 
	if request.GET.has_key('username'): 
		friend = get_object_or_404(User, username=request.GET['username']) 
		friendship = Friendship( 
    		from_friend=request.user, 
    		to_friend=friend 
		)
		
		try:
			friendship.save()
			request.user.message_set.create( message='%s was added to your friend list.' % friend.username )
		except:
			request.user.message_set.create( message='%s is already a friend of yours.' % friend.username )
		
		return HttpResponseRedirect('/friends/%s/' % request.user.username
		)
	else: 
		raise Http404


@login_required
def friend_invite(request): 
  if request.method == 'POST': 
      form = FriendInviteForm(request.POST) 
      if form.is_valid(): 
          invitation = Invitation( 
              name = form.cleaned_data['name'], 
              email = form.cleaned_data['email'], 
              code = User.objects.make_random_password(20), 
              sender = request.user 
          )
          
          invitation.save() # saves invitation
          
          try:
              invitation.send() #tries to send() invitation
              request.user.message_set.create( message='An invitation was sent to %s.' % invitation.email )
          except:
              request.user.message_set.create( message='There was an error while sending the invitation.' )

          return HttpResponseRedirect('/friend/invite/') 
  else: 
      form = FriendInviteForm()
  variables = RequestContext(request, {
          'form': form
  })
  return render_to_response('friends/friend_invite.html', variables)
   

def friend_accept(request, code):
  invitation = get_object_or_404(Invitation, code__exact=code)
  request.session['invitation'] = invitation.id
  return HttpResponseRedirect(reverse('create'))

######################################################################

#tag cloud

def tag_cloud():
	MAX_WEIGHT = 5
	tags = Tag.objects.order_by('name')
	# Calculate tag, min and max counts.
	min_count = max_count = tags[0].articles.count()
	for tag in tags:
		tag.count = tag.articles.count()
		if tag.count < min_count:
			min_count = tag.count
		if max_count < tag.count:
			max_count = tag.count
	# Calculate count range. Avoid dividing by zero.
	range = float(max_count - min_count)
	if range == 0.0:
		range = 1.0
	# Calculate tag weights.
	for tag in tags:
		tag.weight = int(
			MAX_WEIGHT * (tag.count - min_count) / range
		)
	return tags

######################################################################

def add_source(request):
    """docstring for add_source"""

    if request.method=='POST':
        form = AddSourceForm(request.POST) 
        if form.is_valid():
            return HttpResponse(form.cleaned_data['url'])

            #TODO
            #- handle parsing and filling source info here
            #   - check if url is RSS or home page
            #   - parse title, content
            
            import feedparser
            d = feedparser.parse(form.cleaned_data['url'])

            print "New src: %s" % d['feed']['title']

            source = Source(
                name="",
                description="",
                url=form.cleaned_data['url'],
                author=request.user
            )
            source.save()
            
            print "\nParsing ENTRIES:\n"
            for entry in d['entries']:
                article = Article(
                    name=str(entry['title']),
                    description=str(entry['content'][0]['value']),
                    url=str(entry['links'][0]['href']),
                    source=source
                )
                article.save()

    else:
        return render_to_response('source/add.html', {
            'form': AddSourceForm(),
            'tags': tag_cloud()
        },context_instance=RequestContext(request))
    
######################################################################