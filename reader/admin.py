from chameleon.reader.models import *
from chameleon.django.contrib import admin

class SourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ('author',)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ('source',)
    
class FriendshipAdmin(admin.ModelAdmin):
    raw_id_fields = ('to_friend', 'from_friend',)

admin.site.register(Source,SourceAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Friendship,FriendshipAdmin)