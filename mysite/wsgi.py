import os
import sys

# add your project directory to the sys.path
path = '/home/urydope '  # <-- change to your real path
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
