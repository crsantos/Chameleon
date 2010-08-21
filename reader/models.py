from django.db import models
from django.contrib.auth.models import User

###########################################################################

class Source(models.Model):

    name =          models.CharField(max_length=100)
    description =   models.TextField()
    url =           models.URLField(verify_exists=True)
    slug=           models.SlugField(max_length=100, blank=True, unique=True)
    author =        models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/source/"+slug

    class Meta:
        pass

    class Admin:
        search_fields = ['name']

###########################################################################

class Tag(models.Model):
    name =          models.CharField(max_length=100)
    description =   models.TextField()
    slug=           models.SlugField(max_length=100, blank=True, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        pass

    class Admin:
        search_fields = ['name','description']
        
###########################################################################        
        
class Article(models.Model):
    name =          models.CharField(max_length=100)
    description =   models.TextField()
    url =           models.URLField(verify_exists=True)
    slug=           models.SlugField(max_length=100, blank=True, unique=True)
    source=         models.ForeignKey(Source)
    tags=           models.ManyToManyField(Tag, related_name="articles")
    

    def get_absolute_url(self):
       return url 
    
    def __unicode__(self):
        return self.name

    class Meta:
        pass

    class Admin:
        search_fields = ['name', 'description', 'source','url','tags']
        
###########################################################################

class Friendship(models.Model):
	from_friend =   models.ForeignKey(User, related_name='friend_set')
	to_friend =     models.ForeignKey(User, related_name='to_friend_set')

	def __unicode__(self):
		values = {'from' : self.from_friend.username, 'to' : self.to_friend.username }
		return '[%(from)s] friend of [%(to)s]' % values


	class Meta: 
		unique_together = (('to_friend', 'from_friend'), )
		
###########################################################################