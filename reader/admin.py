from chameleon.reader.models import *
from django.contrib import admin

class SourceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Source,SourceAdmin)