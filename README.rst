=======================
Django Loose CMS - Link
=======================

A link plugin for Django Loose CMS.

Requirements
------------

Loose CMS Link plugin requires:

* Django version 1.8
* Python 2.6 or 2.7
* django-loose-cms

Quick Start
-----------

1. Instalation via pip::

    pip install https://github.com/lefterisnik/django-loosecms-link/archive/master.zip

2. Add "loosecms_link" to your INSTALLED_APPS setting after "loosecms" like this::

    INSTALLED_APPS = (
        ...
        'loosecms_link',
    )
    
3. Run ``python manage.py migrate`` to create the loosecms_link models.

4. Run development server ``python manage.py runserver`` and visit http://127.0.0.1:8000/ to start
   playing with the cms.
