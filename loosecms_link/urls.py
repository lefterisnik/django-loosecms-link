# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

app_urlpatterns = [
    url(r'^link/(?P<category_slug>[0-9A-Za-z-_.]+)/(?P<slug>[0-9A-Za-z-_.]+)$', link, name='link-info'),
]

urlpatterns = []
