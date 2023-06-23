"""
ASGI config for AplicatieAdeverinte project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AplicatieAdeverinte.settings')
settings_module = 'AplicatieAdeverinte.production' if 'PRODUCTION' in os.environ else 'AplicatieAdeverinte.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
