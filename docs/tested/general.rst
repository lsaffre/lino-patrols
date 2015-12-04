.. _patrols.tested.general:

General
=======

.. This document is part of the test suite.  
   To test only this  document, run:

    $ python setup.py test -s tests.DocsTests.test_general

    doctest init:

    >>> from __future__ import print_function
    >>> from lino.api.doctest import *

The test database
-----------------


>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
19 apps: lino_startup, staticfiles, about, extjs, jinja, bootstrap3, appypod, printing, system, contenttypes, gfks, users, notifier, changes, office, countries, contacts, patrols, sessions.
22 models:
========================== ======================== ========= =======
 Name                       Default table            #fields   #rows
-------------------------- ------------------------ --------- -------
 changes.Change             changes.Changes          9         0
 contacts.Company           contacts.Companies       22        12
 contacts.CompanyType       contacts.CompanyTypes    7         16
 contacts.Partner           contacts.Partners        19        81
 contacts.Person            contacts.Persons         26        69
 contacts.Role              contacts.Roles           4         0
 contacts.RoleType          contacts.RoleTypes       4         5
 contenttypes.ContentType   gfks.ContentTypes        3         22
 countries.Country          countries.Countries      6         8
 countries.Place            countries.Places         8         78
 gfks.HelpText              gfks.HelpTexts           4         2
 notifier.Notification      notifier.Notifications   7         0
 patrols.Area               patrols.Areas            4         4
 patrols.Employee           patrols.Employees        29        59
 patrols.Member             patrols.Members          3         14
 patrols.Patrol             patrols.Patrols          6         50
 patrols.Team               patrols.Teams            7         7
 patrols.WorkDay            patrols.WorkDays         4         150
 sessions.Session           sessions.SessionTable    3         0
 system.SiteConfig          system.SiteConfigs       4         1
 users.Authority            users.Authorities        3         0
 users.User                 users.Users              13        3
========================== ======================== ========= =======
<BLANKLINE>
