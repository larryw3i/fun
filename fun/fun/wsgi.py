"""
WSGI config for fun project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_py_path = os.path.join( 'settings.py')

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'fun.settings' if os.path.exists(settings_py_path)
                        else 'fun.settings_')

application = get_wsgi_application()
