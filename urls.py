# add custom url config to register our custom page

from django.conf.urls import url
from otree.urls import urlpatterns
from heartbeat.custom_views import heartbeat_setup

# accessing <server>/heartbeat_setup/<session_code>/ offers the input page.
urlpatterns.append(url(r'^heartbeat_setup/(?P<session_code>[a-zA-Z0-9]*)/$', heartbeat_setup, name="heartbeat_setup"))