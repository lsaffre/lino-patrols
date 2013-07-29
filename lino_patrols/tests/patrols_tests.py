# -*- coding: utf-8 -*-
## Copyright 2013 Luc Saffre
## This file is part of the Lino project.
## Lino is free software; you can redistribute it and/or modify 
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## Lino is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with Lino; if not, see <http://www.gnu.org/licenses/>.

"""
This module contains "quick" tests that are run on a demo database 
without any fixture. You can run only these tests by issuing::

  python manage.py test lino_welfare.QuickTest

"""

from __future__ import unicode_literals

import logging
logger = logging.getLogger(__name__)

import decimal

#~ from django.utils import unittest
#~ from django.test.client import Client
from django.conf import settings

#from lino.igen import models
#from lino.modlib.contacts.models import Contact, Companies
#from lino.modlib.countries.models import Country
#~ from lino.modlib.contacts.models import Companies

from django.utils import translation
from django.utils.encoding import force_unicode
from django.core.exceptions import ValidationError

from lino import dd
from lino.utils import i2d
from djangosite.utils.djangotest import RemoteAuthTestCase

#~ contacts = dd.resolve_app('contacts')

DEMO_OVERVIEW = """\
10 applications: sessions, about, contenttypes, system, users, changes, countries, contacts, lino_patrols, djangosite.
30 models:
======================================= ========= =======
 Name                                    #fields   #rows
--------------------------------------- --------- -------
 changes.Change                          9         0
 contacts.Company                        23        12
 contacts.CompanyType                    7         16
 contacts.Partner                        19        81
 contacts.Person                         24        69
 contacts.Role                           4         0
 contacts.RoleType                       4         5
 contenttypes.ConcreteModel              2         0
 contenttypes.ContentType                4         30
 contenttypes.FooWithBrokenAbsoluteUrl   3         0
 contenttypes.FooWithUrl                 3         0
 contenttypes.FooWithoutUrl              2         0
 contenttypes.ProxyModel                 2         0
 countries.City                          8         62
 countries.Country                       6         8
 countries.Language                      5         0
 lino_patrols.Area                       4         4
 lino_patrols.Employee                   28        59
 lino_patrols.Member                     3         14
 lino_patrols.Patrol                     6         50
 lino_patrols.Team                       7         7
 lino_patrols.WorkDay                    4         150
 sessions.Session                        3         4
 system.HelpText                         4         2
 system.SiteConfig                       4         1
 system.TextFieldTemplate                6         2
 users.Authority                         3         0
 users.Membership                        3         0
 users.Team                              4         0
 users.User                              12        3
======================================= ========= =======
"""


class QuickTest(RemoteAuthTestCase):


    def test00(self):
        """
        Initialization.
        """
        #~ print "20130321 test00 started"
        self.user_root = settings.SITE.user_model(username='root',language='en',profile='900')
        self.user_root.save()
        
        
class DemoTest(RemoteAuthTestCase):
    maxDiff = None
    #~ fixtures = 'std demo'.split()
    fixtures = settings.SITE.demo_fixtures
    
    def test001(self):
        """
        test whether the demo fixtures load correctly.
        """
    
        s = settings.SITE.get_db_overview_rst()
        #~ print s
        self.assertEqual(DEMO_OVERVIEW,s)
        
