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
11 apps: sessions, about, bootstrap3, lino, contenttypes, system, users, changes, countries, contacts, lino_patrols.
22 models:
========================== =========================== ========= =======
 Name                       Default table               #fields   #rows
-------------------------- --------------------------- --------- -------
 changes.Change             changes.Changes             9         0
 contacts.Company           contacts.Companies          22        12
 contacts.CompanyType       contacts.CompanyTypes       7         16
 contacts.Partner           contacts.Partners           19        81
 contacts.Person            contacts.Persons            26        69
 contacts.Role              contacts.Roles              4         0
 contacts.RoleType          contacts.RoleTypes          4         5
 contenttypes.ContentType   contenttypes.ContentTypes   4         22
 contenttypes.HelpText      contenttypes.HelpTexts      4         2
 countries.Country          countries.Countries         6         8
 countries.Place            countries.Places            8         78
 lino_patrols.Area          lino_patrols.Areas          4         4
 lino_patrols.Employee      lino_patrols.Employees      29        59
 lino_patrols.Member        lino_patrols.Members        3         14
 lino_patrols.Patrol        lino_patrols.Patrols        6         50
 lino_patrols.Team          lino_patrols.Teams          7         7
 lino_patrols.WorkDay       lino_patrols.WorkDays       4         150
 sessions.Session           sessions.SessionTable       3         0
 system.SiteConfig          system.SiteConfigs          4         1
 system.TextFieldTemplate   system.TextFieldTemplates   5         2
 users.Authority            users.Authorities           3         0
 users.User                 users.Users                 13        3
========================== =========================== ========= =======
<BLANKLINE>
