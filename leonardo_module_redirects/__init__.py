
from django.apps import AppConfig

default_app_config = 'leonardo_module_redirects.Config'

try:
    from local_settings import APPS
except ImportError:
    pass

if 'leonardo_module_redirects' in APPS:
    LEONARDO_APPS = [
        'leonardo_module_redirects',
        'django.contrib.redirects',
    ]

class Config(AppConfig):
    name = 'leonardo_module_redirects'
    verbose_name = "leonardo-module-redirects"
