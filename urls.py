# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    # Add your project's URLs here.
)


## Admin
# Note that you can flatten out this section if you like; at the moment it's
# dynamic and doesn't need to be edited.

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()
    
    if 'django.contrib.admindocs' in settings.INSTALLED_APPS:
        urlpatterns += patterns('',
            url(r'^admin/doc/', include('django.contrib.admindocs.urls'))
        )
    
    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )


## Static Media
# Serve up static media directly from the development server if running in
# DEBUG mode. If you're running this on a staging site behind a proper web
# server, there's no danger in this, since the static media URLs will be picked
# up by that first.

if settings.DEBUG:
    import re
    
    urlpatterns += patterns('django.views.static',
        url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')),
            'serve', {'document_root': settings.MEDIA_ROOT}),
    )