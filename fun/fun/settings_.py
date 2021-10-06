"""
Django settings for fun project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import json
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from os import path

from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1
SITE_DOMAIN = ''
SITE_NAME = ''
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

ALLOWED_HOSTS = ['127.0.0.1'] if DEBUG else ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'crispy_forms',
    # 'django_bootstrap5',
    'crispy_bootstrap5',
    'imagekit',

    'ckeditor',
    'ckeditor_uploader',

    'allauth',
    'allauth.account',

    'funhome.apps.FunhomeConfig',
    'funfile.apps.FunfileConfig',
    'eduhub.apps.EduhubConfig',
    'funuser.apps.FunuserConfig',
    'fun.apps.FunConfig',
    'funauth.apps.FunauthConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'funmiddleware.funmiddleware.TimezoneMiddleware',
]

ROOT_URLCONF = 'fun.urls'

TEMPLATES_DIRS = [
    os.path.join(BASE_DIR, a, 'templates') for a in os.listdir(BASE_DIR)
    if os.path.exists(os.path.join(BASE_DIR, a, 'templates'))
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS + [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
            'libraries':{
            }
        },
    },
]

WSGI_APPLICATION = 'fun.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation' +
            '.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_USER_MODEL = 'funuser.Funuser'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_FROM = ''
DEFAULT_FROM_EMAIL = ''

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_USERNAME_MIN_LENGTH = 2
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
SERVER_EMAIL = ''
LOGIN_REDIRECT_URL = '#'
LOGOUT_REDIRECT_URL = '#'


CRISPY_TEMPLATE_PACK = 'bootstrap5'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

USE_TZ = True

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# values of LANGUAGES and LANGUAGE_CODE are lowercase
LANGUAGES = [('en-us', _('English'))]
LANGUAGE_CODE = 'en-us'

LANGUAGE_COOKIE_AGE = 10 * 365 * 24 * 60 * 60
LANGUAGE_COOKIE_SECURE = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SERVE_STATIC_ROOT = os.path.join(BASE_DIR, 'funstatic')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'funstatic'),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


MEDIA_URL = '/funfile/get_file/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'funfile', 'files')
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ["Format", "Bold", "Italic",
                "Underline", "Strike", "SpellChecker"],
            ['NumberedList', 'BulletedList', "Indent", "Outdent",
                'JustifyLeft', 'JustifyCenter',
                'JustifyRight', 'JustifyBlock'],
            ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink",
                "Subscript", "Superscript"], ['Undo', 'Redo'], ["Source"],
            ["Maximize"]
        ],
        'height': 300,
        'width': '100%',
        'tabSpaces': 4,
        'toolbarCanCollapse': True,
    },
}
CKEDITOR_IMAGE_BACKEND = 'pillow'

DEFAULT_FILE_STORAGE = 'funfile.storage.FunFileStorage'


ADMINS = MANAGERS = ()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {

        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'funlog', 'django_fun.log'),
            'maxBytes': 8 * 1024 * 1024,
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false' if DEBUG
                        else 'require_debug_true'],
        }
    },
    'loggers': {
        'django.request': {
            'handlers': '' if DEBUG else ['mail_admins', 'file', ],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


BLEACH_TAGS = [
    'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p',
    'span', 'img', 'table', 'tbody', 'tr', 'td',
    'strong', 'u', 'ul', 'li',
    'thead', 'th', 'div']
BLEACH_ATTRIBUTES = [
    'class', 'style', 'alt', 'title',
    'data-*', 'width', 'height', 'weight', 'src',
    'href', 'scope']
BLEACH_STYLES = [
    'font', 'font-size', 'align', 'width', 'height', 'weight',
    'padding-*',
    'margin-*', 'border', 'border-color', 'border-radius',
    'background-color', 'color', 'text-align']

SITE_GRAY = False
ALLOWED_REGISTRATION = True

BEIAN_TEXT = ''
BEIAN_URL = ''
