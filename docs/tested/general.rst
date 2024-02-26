.. doctest docs/tested/general.rst
.. _patrols.tested.general:

General
=======

.. This document is part of the test suite.
   To test only this  document, run:

    doctest init:

    >>> import lino
    >>> lino.startup('lino_patrols.settings.demo')
    >>> from lino.api.doctest import *

The test database
-----------------


>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
18 apps: lino, staticfiles, about, jinja, bootstrap3, extjs, printing, system, contenttypes, gfks, users, changes, office, xl, countries, contacts, patrols, sessions.
20 models:
========================== ======================= ========= =======
 Name                       Default table           #fields   #rows
-------------------------- ----------------------- --------- -------
 changes.Change             changes.Changes         10        0
 contacts.Company           contacts.Companies      22        12
 contacts.CompanyType       contacts.CompanyTypes   7         16
 contacts.Partner           contacts.Partners       20        81
 contacts.Person            contacts.Persons        27        69
 contacts.Role              contacts.Roles          4         3
 contacts.RoleType          contacts.RoleTypes      5         5
 contenttypes.ContentType   gfks.ContentTypes       3         20
 countries.Country          countries.Countries     6         10
 countries.Place            countries.Places        9         80
 patrols.Area               patrols.Areas           4         4
 patrols.Employee           patrols.Employees       30        59
 patrols.Member             patrols.Members         3         14
 patrols.Patrol             patrols.Patrols         6         50
 patrols.Team               patrols.Teams           7         7
 patrols.WorkDay            patrols.WorkDays        4         150
 sessions.Session           users.Sessions          3         ...
 system.SiteConfig          system.SiteConfigs      5         1
 users.Authority            users.Authorities       3         0
 users.User                 users.AllUsers          18        3
========================== ======================= ========= =======
<BLANKLINE>
