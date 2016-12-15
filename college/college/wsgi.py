"""
WSGI config for college project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.path.exists('./settings_local.py'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college.settings_local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college.settings")

application = get_wsgi_application()
