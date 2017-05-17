from .base import *

DEBUG = True

# django-debug-toolbar
INSTALLED_APPS += ('debug_toolbar', )
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
INTERNAL_IPS = ('127.0.0.1', )

# django-extensions
INSTALLED_APPS += ('django_extensions', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR('db.sqlite3'),
    }
}
