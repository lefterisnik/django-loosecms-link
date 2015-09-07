# -*- coding: utf-8 -*-
from django import forms
from .models import Link
from loosecms.forms import PluginForm


class LinkForm(PluginForm):

    class Media:
        css ={
            'all': ['loosecms_link/css/loosecms.link.css', ]
        }
        js = ('loosecms_link/js/loosecms.link.js', 'loosecms_link/js/typehead.min.js')

    class Meta(PluginForm.Meta):
        model = Link
        widgets = {
            'type': forms.HiddenInput(),
        }