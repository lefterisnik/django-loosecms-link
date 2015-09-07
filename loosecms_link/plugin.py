# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import LinkForm

from loosecms.plugin_pool import plugin_pool
from loosecms.plugin_modeladmin import PluginModelAdmin, PluginModelInlineAdmin


class LinkInline(PluginModelInlineAdmin):
    model = Link
    fk_name = 'placeholder'
    prepopulated_fields = {'slug': ('title', )}


class LinkManagerPlugin(PluginModelAdmin):
    model = LinkManager
    name = _('Link Container')
    template = "plugin/link.html"
    plugin = True
    inlines = [
        LinkInline,
    ]

    def update_context(self, context, manager):
        links = Link.objects.select_related().filter(placeholder=manager)
        linkscategories = set([link.category for link in links])

        context['links'] = links
        context['linkscategories'] = linkscategories
        return context


class LinkPlugin(PluginModelAdmin):
    change_form_template = None
    delete_confirmation_template = None
    model = Link
    name = _('Links')
    form = LinkForm
    plugin_cke = True
    template_cke = "plugin/ckeditor/link.html"
    prepopulated_fields = {'slug': ('title', )}

    def get_urls(self):
        urls = super(LinkPlugin, self).get_urls()
        link_api_urls = [
            url(r'^api/get_title/$', self.admin_site.admin_view(self.get_title), name='get_title'),
            url(r'^api/get_url/$', self.admin_site.admin_view(self.get_url), name='get_url'),
        ]

        return link_api_urls + urls

    def get_title(self, request):
        if 'title' in request.GET:
            title = request.GET['title']
            titles = self.model.objects.filter(title__icontains=title).values('title')
        else:
            titles = self.model.objects.all().values('title')
        return JsonResponse(list(titles), safe=False)

    def get_url(self, request):
        if 'url' in request.GET:
            url = request.GET['url']
            urls = self.model.objects.filter(url__icontains=url).values('url')
        else:
            urls = self.model.objects.all().values('url')
        return JsonResponse(list(urls), safe=False)


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "placeholder":
            kwargs["queryset"] = LinkManager.objects.all()
        return super(LinkPlugin, self).formfield_for_foreignkey(db_field, request, **kwargs)


plugin_pool.register_plugin(LinkManagerPlugin)
plugin_pool.register_plugin(LinkPlugin)