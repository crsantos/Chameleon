import os, sys

sys.path.append('/home/client15/web69/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chameleon.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
