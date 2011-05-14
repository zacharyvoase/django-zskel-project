# -*- coding: utf-8 -*-

import django
import logging
import warnings; warnings.simplefilter("ignore") # for the `path` module.
from path import path
import sys


## Project

PROJECT_DIR = path(__file__).abspath().realpath().dirname().parent
PROJECT_NAME = PROJECT_DIR.basename()
SITE_DIR = PROJECT_DIR.parent

sys.path.append(SITE_DIR)
sys.path.append(PROJECT_DIR / 'apps')
sys.path.append(PROJECT_DIR / 'libs')

ADMINS = (
    ('Zachary Voase', 'z@zacharyvoase.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
USE_I18N = False
USE_L10N = True

SITE_ID = 1

## Replace this in every installation. It should be a random sequence of about
## 50 characters, and should not be shared with anyone.
SECRET_KEY = 1/0


## Media

MEDIA_ROOT = PROJECT_DIR / 'media' / '' # Ensure it has a trailing slash.
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
ADMIN_MEDIA_ROOT = path(django.__file__).abspath().dirname() / 'contrib' / 'admin' / 'media'


## Templates

# DEFAULT_CONTENT_TYPE = 'text/html'
DEFAULT_CONTENT_TYPE = 'application/xhtml+xml'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
#   'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    PROJECT_DIR / 'templates',
)


## Request processing

ROOT_URLCONF = PROJECT_NAME + '.urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

CACHE_MIDDLEWARE_SECONDS = 5
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_NAME + '_'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False


## Installed applications

INSTALLED_APPS = (
    ## Django contrib apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',

    ## Third-party apps
    'debug_toolbar',

    ## Local apps
    # Nothing here yet.
)


## Logging

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'
LOG_FORMATTER = logging.Formatter(
    u'%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt=LOG_DATE_FORMAT)

CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)
CONSOLE_HANDLER.setLevel(logging.DEBUG)

logging.root.addHandler(CONSOLE_HANDLER)
logging.root.setLevel(logging.WARN) # Default level.


## Django Debug Toolbar

INTERNAL_IPS = ('127.0.0.1', )

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}
