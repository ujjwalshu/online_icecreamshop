"""
WSGI config for Hello project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.handlers.wsgi import WSGIHandler  # Import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hello.settings')

application: WSGIHandler = get_wsgi_application()

