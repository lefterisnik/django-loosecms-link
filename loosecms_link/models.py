# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db import models
from loosecms.models import Plugin


class LinkManager(Plugin):
    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give the name of the link manager.'))
    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


class LinkCategory(models.Model):
    title = models.CharField(_('title'), max_length=100,
                             help_text=_('Give the name of the category'))

    def __unicode__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(_('title'), max_length=100,
                             help_text=_('Give the name of the link.'))
    category = models.ForeignKey(LinkCategory, verbose_name=_('category'),
                                 help_text=_('Select the category.'))
    manager = models.ForeignKey(LinkManager, verbose_name=_('manager'),
                                help_text=_('Select the manager.'))
    url = models.CharField(_('url'), max_length=200,
                           help_text=_('Give the url of the link.'))
    order = models.IntegerField(_('order'))

    published = models.BooleanField(_('published'), default=True)

    def __unicode__(self):
        return self.title
