# Django settings for chameleon project.

import os
import platform

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Carlos Santos', 'carlosricardosantos@gmail.com'),
)

MANAGERS = ADMINS
INTERNAL_IPS = ('127.0.0.1',)
DEPLOYMENT_SERVERS = ["crop.floodbit.org"]
DEVELOPMENT_MODE = not (platform.node() in DEPLOYMENT_SERVERS)
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
ITEMS_PER_PAGE=5
LAST_X_DAYS=10


DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL+'admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e_me8mun&r^310&%5+q5l5czdz^r%2f*es6i=i1zuw2-niu9_l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL="/"
ROOT_URLCONF = 'chameleon.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    # 'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'chameleon.reader',
    #'south',
)



if DEVELOPMENT_MODE:


    DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = 'chameleon.db'             # Or path to database file if using sqlite3.
    DATABASE_USER = ''             # Not used with sqlite3.
    DATABASE_PASSWORD = ''         # Not used with sqlite3.
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

    # Absolute path to the directory that holds media.
    # Example: "/home/media/media.lawrence.com/"
    MEDIA_ROOT = '/Users/crsantos/dev/chameleon/media'

    #ROOT_URLCONF = 'chameleon.urls'

    SITE_HOST = '127.0.0.1:8080'

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        [os.path.join(os.path.dirname(__file__), "templates")]
    )

else:

    DEBUG = False
    CACHE_BACKEND = 'db://cache_table'


    DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
    DATABASE_NAME = ''             # Or path to database file if using sqlite3.
    DATABASE_USER = ''             # Not used with sqlite3.
    DATABASE_PASSWORD = ''         # Not used with sqlite3.
    DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
    DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.



    MEDIA_ROOT = '/home/client15/web69/chameleon/media'
    #ROOT_URLCONF = 'chameleon.apache.urls'
    SITE_HOST = 'cenas.crsantos.info'

    TEMPLATE_DIRS = (
        '/home/client15/web69/chameleon/templates',
    )

    DEFAULT_FROM_EMAIL = 'Chameleon <someone@whatever.domain.com>'
    #EMAIL_USE_TLS = True
    EMAIL_HOST = 'localhost'
    #EMAIL_HOST_USER = ''
    #EMAIL_HOST_PASSWORD = ''
    #EMAIL_PORT = 587


