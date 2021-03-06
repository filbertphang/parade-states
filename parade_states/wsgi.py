"""
WSGI config for parade_states project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parade_states.settings')

application = get_wsgi_application()

# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
