# -*- coding: UTF-8 -*-
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

import os

from lino.projects.std.settings import *
import lino_patrols
from lino_patrols import SETUP_INFO as setup_info

class Site(Site):
  
    version = setup_info['version'] 
    url = setup_info['url'] # "http://code.google.com/p/lino-welfare/"
    verbose_name = "Lino Patrols"
    
    demo_fixtures = 'std demo demo2'.split()
    
    auto_configure_logger_names = 'lino lino_patrols'
    
    userdocs_prefix = 'patrols.'
    
    #~ project_model = 'contacts.Person'
    #~ project_model = 'pcsw.Client'
    
    #~ accounts_ref_length = 5
    
    #~ languages = ('de', 'fr', 'nl', 'en')
    languages = "de fr en"
    
    #~ index_view_action = "pcsw.Home"
    
    def setup_quicklinks(self, ar, tb):
        tb.add_action('patrols.Patrols')
        self.on_each_app('setup_quicklinks', ar, tb)
        
    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
            
        yield 'lino.modlib.contenttypes'
        yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino.modlib.changes'
        yield 'lino.modlib.countries'
        yield 'lino.modlib.contacts'
        
        yield 'lino_patrols.patrols'
        
        
      

#~ SITE = Site(globals())

#~ LOGGING['logger_names'] = 'djangosite lino lino_patrols'
#~ LOGGING.update(loggers='djangosite lino lino_welfare')
#~ print 20130409, __file__, LOGGING

#~ TIME_ZONE = 'Europe/Brussels'
#~ TIME_ZONE = None
#~ print 20130613, __file__
