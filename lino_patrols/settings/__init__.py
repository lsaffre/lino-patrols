# -*- coding: UTF-8 -*-
# Copyright 2013-2015 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)

import os

from lino.projects.std.settings import *
import lino_patrols
from lino_patrols import SETUP_INFO as setup_info


class Site(Site):

    version = setup_info['version']
    url = setup_info['url']  # "http://code.google.com/p/lino-welfare/"
    verbose_name = "Lino Patrols"

    demo_fixtures = 'std demo demo2'.split()

    auto_configure_logger_names = 'atelier lino lino_patrols'

    userdocs_prefix = 'patrols.'

    #~ project_model = 'contacts.Person'
    #~ project_model = 'pcsw.Client'

    #~ accounts_ref_length = 5

    #~ languages = ('de', 'fr', 'nl', 'en')
    languages = "de fr en"

    #~ index_view_action = "pcsw.Home"

    def setup_quicklinks(self, user, tb):
        tb.add_action('patrols.Patrols')
        self.on_each_app('setup_quicklinks', user, tb)

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()

        yield 'lino.modlib.gfks'
        yield 'lino.modlib.users'
        yield 'lino.modlib.changes'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.contacts'

        yield 'lino_patrols.patrols'


#~ SITE = Site(globals())

#~ LOGGING['logger_names'] = 'djangosite lino lino_patrols'
#~ LOGGING.update(loggers='djangosite lino lino_welfare')
#~ print 20130409, __file__, LOGGING

#~ TIME_ZONE = 'Europe/Brussels'
#~ TIME_ZONE = None
#~ print 20130613, __file__
