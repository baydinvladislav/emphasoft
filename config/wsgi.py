import os
import sys
import platform

#путь к проекту
sys.path.insert(0, '/home/c/cd65092/new-site/public_html/djangosite')
#путь к фреймворку
sys.path.insert(0, '/home/c/cd65092/new-site/public_html/djangosite/config')
#путь к виртуальному окружению
sys.path.insert(0, '/home/c/cd65092/new-site/public_html/myenv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()