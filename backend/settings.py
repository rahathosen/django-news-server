from pathlib import Path
import os
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '*']

SESSION_COOKIE_SECURE = False

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third party apps
    'graphene_django',
    'ckeditor',
    "cloudvault",

    # Created apps
    'advertisement',
    'article',
    'categories',
    'news',
    'reporter',
    'webInfo',
    'feature',

]

if DEBUG:
    INSTALLED_APPS += [
    # Third party apps 
    'import_export',

    # Created apps
    'search',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES_DIRS = os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.app'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# Database Sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'udayan.db',
    }
}

# # for railway
# DATABASES = {
#     'default': {
#         'ENGINE': os.environ['PGENGINE'],
#         'URL': os.environ['DATABASE_URL'],
#         'NAME': os.environ['PGDATABASE'],
#         'USER': os.environ['PGUSER'],
#         'PASSWORD': os.environ['PGPASSWORD'],
#         'HOST': os.environ['PGHOST'],
#         'PORT': os.environ['PGPORT'],
       
#     }
# }


if DEBUG: 
    AUTH_PASSWORD_VALIDATORS = []
else:
    AUTH_PASSWORD_VALIDATORS = [
    
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Path where media is stored
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

# Base url to serve media files
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GRAPHENE = {
    "SCHEMA": "backend.schema.schema"
}


DEFAULT_FILE_STORAGE = "cloudvault.cloud_storage.CloudinaryStorage"
# Configure Cloudinary
CLOUDINARY = {
    "cloud_name": os.environ['CLOUD_NAME'],
    "api_key": os.environ['API_KEY'],
    "api_secret": os.environ['API_SECRET']

}
# CSRF_TRUSTED_ORIGINS = [ 
#     'https://dailyudayan.com',
#     'https://www.dailyudayan.com',
#     'http://dailyudayan.com',

# ]