"""
Django settings for fun project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

"""
051020200027
.env and appconf.json was deprecated, yaml is been used.
"""

import os
import sys
import json
import yaml
from django.utils.translation import gettext_lazy as _
from os import path


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


app_env_path = path.join( BASE_DIR, '.env.yaml' )
funlog_dir =  os.path.join(BASE_DIR, 'funlog')
funlog_path =  os.path.join( funlog_dir,  'django_fun.log')


if not path.exists( funlog_path ):
    os.makedirs( funlog_dir )
    open(funlog_path, 'a' ).close()


if not path.exists( app_env_path ):
    raise Exception(
        'You should custon your .env.yaml file to keep app run normally')


with open( app_env_path, 'r' ) as f:
    app_env = yaml.safe_load( f )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = app_env['env']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = app_env['debug']

SITE_ID = 1

ALLOWED_HOSTS = ['*', ]

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
    'imagekit',

    'ckeditor',
    'ckeditor_uploader',

    'allauth',
    'allauth.account',

    'funhome.apps.FunhomeConfig',
    'funfile.apps.FunfileConfig',
    'eduhub.apps.EduhubConfig',
    'funuser.apps.FunuserConfig',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
                'funtag': 'funtag.templatetag',
            }
        },
    },
]


WSGI_APPLICATION = 'fun.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # psql
    'default': {
        'ENGINE': app_env['database']['engine'],
        'NAME': app_env['database']['name'],
        'USER': app_env['database']['user'],
        'PASSWORD': app_env['database']['password'],
        'HOST': app_env['database']['host'],
        'PORT': app_env['database']['port']
    },
    'sqlite3': {
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

# 'allauth.account.auth_backends.AuthenticationBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# ACCUNT_AND_EMAIL

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


EMAIL_HOST = app_env['email']['host']
EMAIL_HOST_USER =  app_env['email']['user']
EMAIL_HOST_PASSWORD =  app_env['email']['password']
EMAIL_PORT =  app_env['email']['port']
EMAIL_USE_SSL =  app_env['email']['use_ssl']
EMAIL_FROM =  app_env['email']['from']
DEFAULT_FROM_EMAIL =  app_env['email']['from']

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_USERNAME_MIN_LENGTH = 2


SERVER_EMAIL = app_env['email']['from']

LOGIN_REDIRECT_URL = '#'
LOGOUT_REDIRECT_URL = '#'


# END ACCUNT_AND_EMAIL

CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

USE_TZ = True

TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')  # 'UTC' # 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

LANGUAGE_CODE = 'zh-hans'

LANGUAGE_COOKIE_AGE = 10*365*24*60*60
LANGUAGE_COOKIE_SECURE = app_env['language_cookie_secure']

LANGUAGES = (
    ('en', _('English')),
    ('zh-hans', _('中文简体')),
    # ('zh-hant', _('中文繁體')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# FOR NGINX
STATIC_ROOT = os.path.join(BASE_DIR,   'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'funstatic'),
]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# MEDIA_FILE
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
# END MEDIA_FILE

# FILE_STORAGE
DEFAULT_FILE_STORAGE = 'funfile.storage.FunFileStorage'
# END FILE_STORAGE


# LOGGING

MANAGERS = app_env['developers']

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
            'filename': funlog_path,
            'maxBytes': 8*1024*1024,
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

# END_LOGGING

# BLEACH
BLEACH_TAGS = [
    'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p',
               'span', 'img', 'table', 'tbody', 'tr', 'td', 'thead', 'th']
BLEACH_ATTRIBUTES = [
    'class', 'style', 'alt', 'title',
    'data-*', 'width', 'height', 'weight', 'src',
    'href', 'scope']
BLEACH_STYLES = [
    'font', 'font-size', 'align', 'width', 'height', 'weight',
    'padding-*',
    'margin-*', 'border', 'border-color', 'border-radius',
    'background-color', 'color', 'text-align']
# ENDBLEACH
