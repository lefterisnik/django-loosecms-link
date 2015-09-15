# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from loosecms.models import Plugin


#TODO: Add pre-save when one url change change the same url in database

class LinkManager(Plugin):
    default_type = 'LinkManagerPlugin'

    title = models.CharField(_('title'), max_length=200,
                             help_text=_('Give the name of the link manager.'))
    ctime = models.DateTimeField(auto_now_add=True)

    utime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)


class LinkCategory(models.Model):
    title = models.CharField(_('title'), max_length=100,
                             help_text=_('Give the name of the category.'))
    slug = models.SlugField(_('slug'), unique=True,
                            help_text=_('Give the unique indentified of the category.'))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('link category')
        verbose_name_plural = _('link categories')


class Link(Plugin):
    BLANK = '_blank'
    SELF = '_self'
    PARENT = '_parent'
    TOP = '_top'
    choices = (
        (BLANK, 'New window or tab'),
        (SELF, 'Same frame'),
        (PARENT, 'Parent frame'),
        (TOP, 'Current window'),
    )
    default_type = 'LinkPlugin'

    title = models.CharField(_('title'), max_length=100,
                             help_text=_('Give the name of the link.'))
    slug = models.SlugField(_('slug'), unique=True,
                            help_text= _('Give the unique identifier.'))
    category = models.ForeignKey(LinkCategory, verbose_name=_('category'),
                                 help_text=_('Select the category.'))
    url = models.CharField(_('url'), max_length=200,
                           help_text=_('Give the url of the link.'))
    open = models.CharField(_('open'), max_length=50, choices=choices, default=SELF,
                            help_text=_('Specify where to open the linked document'))
    order = models.IntegerField(_('order'))

    def __unicode__(self):
        return "%s (%s)" %(self.title, self.type)

    class Meta:
        verbose_name = _('link')
        verbose_name_plural = _('links')
