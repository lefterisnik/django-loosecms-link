# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.template import loader
from django.contrib import admin

from .forms import *
from .models import *

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin


class LinkInline(admin.StackedInline):
    model = Link
    extra = 1


class LinkPlugin(PluginModelAdmin):
    model = LinkManager
    name = _('External links')
    form = LinkManagerForm
    template = "plugin/link.html"
    plugin = True
    inlines = [
        LinkInline,
    ]
    extra_initial_help = None
    fields = ('type', 'placeholder', 'title', 'published')

    def render(self, context, manager):
        '''
        Get all link and categories
        '''
        links = Link.objects.select_related().filter(manager=manager)
        linkscategories = set([link.category for link in links])

        t = loader.get_template(self.template)
        context['links'] = links
        context['linkscategories'] = linkscategories
        return t.render(context)

    def get_changeform_initial_data(self, request):
        initial = {}
        if self.extra_initial_help:
            initial['type'] = self.extra_initial_help['type']
            initial['placeholder'] = self.extra_initial_help['placeholder']
            initial['manager'] = self.extra_initial_help['page']

            return initial
        else:
            return {'type': 'LinkPlugin'}


plugin_pool.register_plugin(LinkPlugin)