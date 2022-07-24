
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'c033077e40698b647e23e50881c4d22f'
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory_db',     # Database Name
        'USER': 'postgres',       # User Name
        'PASSWORD': 'root',         # Password for Postgresql
        'HOST': '127.0.0.1',  # Django Server
        'PORT': '5432',             # default port for Postgresql
    }
}

# Added Static Setting For local Machine

# Added Static Setting For local Machine

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media")

