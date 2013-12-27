.. _patrols.tested.general:

General
=======

.. include:: /include/tested.rst

Some tests:
  
>>> from __future__ import print_function
>>> from lino.runtime import *
>>> from django.utils import translation
>>> from pprint import pprint

The test database
-----------------

Test whether :meth:`get_db_overview_rst 
<lino_site.Site.get_db_overview_rst>` returns the expected result:

>>> print(settings.SITE.get_db_overview_rst()) 
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
10 applications: sessions, about, contenttypes, system, users, changes, countries, contacts, lino_patrols, djangosite.
24 models:
========================== ========= =======
 Name                       #fields   #rows
-------------------------- --------- -------
 changes.Change             9         0
 contacts.Company           23        12
 contacts.CompanyType       7         16
 contacts.Partner           19        81
 contacts.Person            24        69
 contacts.Role              4         0
 contacts.RoleType          4         5
 contenttypes.ContentType   4         24
 countries.Country          6         8
 countries.Place            8         75
 lino_patrols.Area          4         4
 lino_patrols.Employee      28        59
 lino_patrols.Member        3         14
 lino_patrols.Patrol        6         50
 lino_patrols.Team          7         7
 lino_patrols.WorkDay       4         150
 sessions.Session           3         0
 system.HelpText            4         2
 system.SiteConfig          4         1
 system.TextFieldTemplate   6         2
 users.Authority            3         0
 users.Membership           3         0
 users.Team                 4         0
 users.User                 13        3
========================== ========= =======
<BLANKLINE>


