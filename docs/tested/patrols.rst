.. _patrols.tested.patrols:

Patrols
=======

.. include:: /include/tested.rst

The following statement imports a set of often-used global names::

>>> from lino.runtime import *

We can now refer to every installed app via it's `app_label`.
For example here is how we can verify here that the demo database 
has three patrols and four areas:

>>> patrols.Patrol.objects.count()
3
>>> patrols.Area.objects.count()
4

