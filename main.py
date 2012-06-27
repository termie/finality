import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'final.settings'

import django.core.handlers.wsgi
app = django.core.handlers.wsgi.WSGIHandler()
