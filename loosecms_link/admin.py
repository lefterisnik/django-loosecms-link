# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Link, LinkCategory, LinkManager
from .plugin import LinkPlugin

admin.site.register(LinkManager, LinkPlugin)
admin.site.register(LinkCategory)
admin.site.register(Link)
