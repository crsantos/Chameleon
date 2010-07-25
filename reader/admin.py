from chameleon.reader.models import *
from django.contrib import admin

class SourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ('author',)

admin.site.register(Source,SourceAdmin)