from __future__ import absolute_import, unicode_literals
import os
from os.path import join, dirname


PROJECT_PATH = dirname(dirname(dirname(__file__)))
APPS_PATH = join(PROJECT_PATH, "apps")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'm6c-&_17ki^f4z_2icp^@$yuy$@5u$%fu=4x7857ho=y%-m8lw'

DEBUG = True

ALLOWED_HOSTS = []

# App django
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

# App de Terceros
THIRD_PARTY_APPS = (
    # Para dar estilos usando bootstrap a los campos de los formularios
    # 'bootstrap3',
    # 'django.contrib.humanize',
    # 'easy_pdf',
)

# Apps Locales
LOCAL_APPS = (
    # apps locales
    'apps.motorcycle',
    'apps.assistant',
    'apps.business',
    'apps.personal',
    'apps.promotions',
    'apps.replacement',
    'apps.sale',
    'apps.usuario',
    'apps.reparacion',
    'apps.messaging',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sanbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
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


WSGI_APPLICATION = 'sanbot.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'BDmotos'),
    }
}


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

LANGUAGE_CODE = 'es-BO'

TIME_ZONE = 'America/La_Paz'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
MEDIA_ROOT = join(PROJECT_PATH, 'public/media/')
MEDIA_URL = '/media/'

# PLATFORM SETTINGS
# ------------------------------------------------------------------------------
PROJECT_NAME = "MBOT"
PROJECT_AUTHOR = "GITBO"
PROJECT_DOMAIN = "http://gitbo.xyz"

