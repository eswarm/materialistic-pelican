#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eswar Malla'
SITENAME = u"Eswar's log"
SITEURL = '.'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/eswarm'),
		  ('Google plus', 'https://plus.google.com/102630360601349400454/about'),
          ('Twitter', 'https://twitter.com/eswar_001'))

DEFAULT_PAGINATION = 4

#NAVBAR_COLOR = '#263238'
PRIMARY_COLOR = 'indigo'
ACCENT_COLOR = 'light blue'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USER_LOGO_URL = SITEURL + '/images/logo.png'
