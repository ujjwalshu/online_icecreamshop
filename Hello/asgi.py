"""
ASGI config for Hello project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from django.core.handlers.asgi import ASGIHandler  # Import ASGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hello.settings')

application: ASGIHandler = get_asgi_application()
