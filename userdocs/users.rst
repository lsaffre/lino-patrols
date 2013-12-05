.. _patrols.users:

========================
Gestion des utilisateurs
========================


Référence
=========

.. actor:: users.Users
.. actor:: users.Teams
.. actor:: users.Memberships


.. _patrols.users.User.profile:

The profile of a user
---------------------

Each user must have a profile in order to be active. 
Users with an empty :ref:`patrols.users.User.profile` 
field are considered inactive and cannot log in.



Team
====

The permissions do not depend on the Team, 
they depend on the :ref:`patrols.users.UserProfile`.
Belonging to a user group or not has no influence on access permissions


Teams
=============


The table of available :ddref:`patrols.users.Team` records on this site.

The demo site has the following teams:

.. django2rst:: settings.SITE.login('robin').show(users.Teams)



Membership
=============


A membership is when a given :ref:`patrols.users.User` 
belongs to a given :ref:`patrols.users.Team`.



.. _patrols.users.UserProfile:

User Profile
=============

A user profile is a combination of access rights and permission sets. 

.. actor:: lino.UserProfiles


User Profiles
=============

The list of user profiles available on this site. 

.. django2rst:: settings.SITE.login('robin').show(lino.UserProfiles)




Reference
=========


.. actor:: system.ContentTypes
