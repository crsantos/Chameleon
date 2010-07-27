from django.db import models
from django.contrib.auth.models import User

class Source(models.Model):

    name =          models.CharField(max_length=100)
    description =   models.TextField()
    url =           models.URLField(verify_exists=True)
    slug=           models.SlugField(max_length=100, blank=True, unique=True)
    author =        models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    # def get_absolute_url(self):
    #     return "/source/"+str(self.id)

    class Meta:
        pass

    class Admin:
        search_fields = ['name']


class Tag(models.Model):
    name =          models.CharField(max_length=100)
    description =   models.TextField()
    slug=           models.SlugField(max_length=100, blank=True, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        pass

    class Admin:
        search_fields = ['name']
        
class Article(models.Model):
    name =          models.CharField(max_length=100)
    description =   models.TextField()
    url =           models.URLField(verify_exists=True)
    slug=           models.SlugField(max_length=100, blank=True, unique=True)
    source=         models.ForeignKey(Source)
    
    def __unicode__(self):
        return self.name

    class Meta:
        pass

    class Admin:
        search_fields = ['name', 'description', 'source']