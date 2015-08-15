# -*- coding:utf-8 -*-
from django import forms
from .models import LinkManager, Link
from loosecms.forms import PluginForm


class LinkManagerForm(PluginForm):

    class Meta(PluginForm.Meta):
        model = LinkManager
