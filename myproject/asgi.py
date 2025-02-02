"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

setting_module='university.deployment'if 'RENDER_EXTEND':
os.environ.setdefault('DJANGO _SETTINGS_MODULE',setting_module)

application = get_asgi_application()
