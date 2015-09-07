# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Link, LinkCategory
from .plugin import LinkPlugin


class LinkCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(LinkCategory, LinkCategoryAdmin)
admin.site.register(Link, LinkPlugin)
