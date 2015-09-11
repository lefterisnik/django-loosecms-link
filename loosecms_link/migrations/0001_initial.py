# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loosecms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text='Give the name of the link.', max_length=100, verbose_name='title')),
                ('slug', models.SlugField(help_text='Give the unique identifier.', unique=True, verbose_name='slug')),
                ('url', models.CharField(help_text='Give the url of the link.', max_length=200, verbose_name='url')),
                ('open', models.CharField(default=b'_self', help_text='Specify where to open the linked document', max_length=50, verbose_name='open', choices=[(b'_blank', b'New window or tab'), (b'_self', b'Same frame'), (b'_parent', b'Parent frame'), (b'_top', b'Current window')])),
                ('order', models.IntegerField(verbose_name='order')),
            ],
            bases=('loosecms.plugin',),
        ),
        migrations.CreateModel(
            name='LinkCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Give the name of the category.', max_length=100, verbose_name='title')),
                ('slug', models.SlugField(help_text='Give the unique indentified of the category.', unique=True, verbose_name='slug')),
            ],
        ),
        migrations.CreateModel(
            name='LinkManager',
            fields=[
                ('plugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='loosecms.Plugin')),
                ('title', models.CharField(help_text='Give the name of the link manager.', max_length=200, verbose_name='title')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('utime', models.DateTimeField(auto_now=True)),
            ],
            bases=('loosecms.plugin',),
        ),
        migrations.AddField(
            model_name='link',
            name='category',
            field=models.ForeignKey(verbose_name='category', to='loosecms_link.LinkCategory', help_text='Select the category.'),
        ),
    ]
