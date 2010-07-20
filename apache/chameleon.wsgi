import os, sys

sys.path.append('')
os.environ['DJANGO_SETTINGS_MODULE'] = 'chameleon.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
