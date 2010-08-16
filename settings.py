# Django settings for chameleon project.

import os
import platform

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

DEPLOYMENT_SERVERS = [""]

DEVELOPMENT_MODE = not (platform.node() in DEPLOYMENT_SERVERS)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

ITEMS_PER_PAGE=5

LAST_X_DAYS=10

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vhw0!w*7k2jcz5r2sanlm@ygn+psp5fa&06#fpczw2fj7fr8i('

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

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
#ADMIN_MEDIA_PREFIX = '/media/'
ADMIN_MEDIA_PREFIX = MEDIA_URL+'admin/'

ACCOUNT_ACTIVATION_DAYS=7

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'reader',
    'south',
)

# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.contrib.messages.context_processors.messages",
# )


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL="/"

if DEVELOPMENT_MODE:

    DATABASES = {
        'default': {
            'ENGINE': 'sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'chameleon.db',          # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

    # Absolute path to the directory that holds media.
    # Example: "/home/media/media.lawrence.com/"
    MEDIA_ROOT = '/Users/crsantos/dev/chameleon/media'

    ROOT_URLCONF = 'chameleon.urls'

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
    
    DATABASE_ENGINE = 'mysql'
    DATABASE_NAME = 'FILL_HERE'
    DATABASE_USER = 'FILL_HERE'
    DATABASE_PASSWORD = 'FILL_HERE'

    MEDIA_ROOT = ''

    ROOT_URLCONF = 'chameleon.apache.urls'
    SITE_HOST = ''


    TEMPLATE_DIRS = (
        '',
    )

    DEFAULT_FROM_EMAIL = 'Sender <someone@whatever.domain.com>'
    #EMAIL_USE_TLS = True
    EMAIL_HOST = 'localhost'
    #EMAIL_HOST_USER = ''
    #EMAIL_HOST_PASSWORD = ''
    #EMAIL_PORT = 587