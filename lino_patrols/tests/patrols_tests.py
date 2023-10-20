# -*- coding: utf-8 -*-
# Copyright 2013 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)

"""
This module contains "quick" tests that are run on a demo database
without any fixture. You can run only these tests by issuing::

  python manage.py test lino_patrols.QuickTest

"""

from lino import logger

import decimal

#~ from django.utils import unittest
#~ from django.test.client import Client
from django.conf import settings

#from lino.igen import models
#from lino_xl.lib.contacts.models import Contact, Companies
#from lino_xl.lib.countries.models import Country
#~ from lino_xl.lib.contacts.models import Companies

from django.utils import translation
from django.utils.encoding import force_str
from django.core.exceptions import ValidationError

from lino.api import dd, rt
from lino.utils import i2d
from lino.utils.djangotest import RemoteAuthTestCase

#~ contacts = dd.resolve_app('contacts')


class QuickTest(RemoteAuthTestCase):

    def test00(self):
        """
        Initialization.
        """
        #~ print "20130321 test00 started"
        self.user_root = settings.SITE.user_model(
            username='root', language='en', profile='900')
        self.user_root.save()


class DemoTest(RemoteAuthTestCase):
    maxDiff = None
    fixtures = settings.SITE.demo_fixtures

    def test001(self):
        """
        test whether the demo fixtures load correctly.
        """
        self.assertEqual(1+1, 2)
