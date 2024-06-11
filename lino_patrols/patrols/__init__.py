# Copyright 2013-2014 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)
"""
The :mod:`lino_patrols.patrols` package provides models and
functionality for managing patrols.

.. autosummary::
   :toctree:

    models

"""

from lino import ad, _


class Plugin(ad.Plugin):

    verbose_name = _("Patrols")

    def setup_main_menu(self, site, profile, m, ar=None):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action('patrols.Areas')
        m.add_action('patrols.Employees')
        m.add_action('patrols.EmployeesByWeek')
        m.add_action('patrols.Teams')
        m.add_action('patrols.Patrols')
        #~ m.add_action('patrols.Days')

    def setup_explorer_menu(self, site, profile, m, ar=None):
        m = m.add_menu(self.app_label, self.verbose_name)
        m.add_action(site.modules.patrols.WorkDayTypes)
        m.add_action('patrols.WorkDays')
        m.add_action('patrols.Members')
