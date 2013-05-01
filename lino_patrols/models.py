# -*- coding: UTF-8 -*-
## Copyright 2008-2013 Luc Saffre
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
Contains PCSW-specific models and tables that have not yet been 
moved into a separate module because they are really very PCSW specific.

"""

import logging
logger = logging.getLogger(__name__)

import os
import datetime

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.exceptions import MultipleObjectsReturned
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import string_concat
from django.utils.encoding import force_unicode 
from django.utils.functional import lazy

from lino import dd

from lino.mixins.printable import DirectPrintAction, Printable
#~ from lino.mixins.reminder import ReminderEntry
from lino.core import actions
#~ from lino.core import changes


contacts = dd.resolve_app('contacts')
countries = dd.resolve_app('countries')

class Area(dd.BabelNamed):
    
    class Meta:
        verbose_name = _("Area") 
        verbose_name_plural = _("Areas")
        
class Areas(dd.Table):
    model = Area
    detail_layout = """
    id name 
    PatrolsByArea
    """
    

class Team(dd.BabelNamed):
    
    class Meta:
        verbose_name = _("Team") 
        verbose_name_plural = _("Teams") 
    
    active_from = models.DateField(verbose_name=_("Active from"),null=True,blank=True)
    active_until = models.DateField(verbose_name=_("until"),null=True,blank=True)

class Teams(dd.Table):
    model = Team
    detail_layout = """
    id name active_from active_until
    PatrolsByTeam
    """
    
class Patrol(dd.Model):
    
    class Meta:
        verbose_name = _("Patrol") 
        verbose_name_plural = _("Patrols") 
    
    date = models.DateField(verbose_name=_("Date"))
    area = models.ForeignKey(Area)
    team = models.ForeignKey(Team)
    
class Patrols(dd.Table):
    model = Patrol
    parameters = dict(
      dates_from = models.DateField(verbose_name=_("Dates from"),null=True,blank=True),
      dates_until = models.DateField(verbose_name=_("until"),null=True,blank=True),
    )
    
    @classmethod
    def get_request_queryset(self,ar):
        qs = super(Patrols,self).get_request_queryset(ar)
        if ar.param_values.dates_from:
            qs = qs.filter(date__gte=ar.param_values.dates_from)
        if ar.param_values.dates_until:
            qs = qs.filter(date__lte=ar.param_values.dates_until)
        return qs
  
    @classmethod
    def get_title_tags(self,ar):
        for t in super(Patrols,self).get_title_tags(ar):
            yield t
        if ar.param_values.dates_from:
            if ar.param_values.dates_until:
                yield "%s-%s" % (ar.param_values.dates_from,ar.param_values.dates_until)
            else:
                yield _("-%s") % ar.param_values.dates_until
        yield _("%s-") % ar.param_values.dates_from
    
    
class PatrolsByTeam(Patrols):
    master_key = 'team'    
    
class PatrolsByArea(Patrols):
    master_key = 'area'    
    
    


MODULE_LABEL = _("Patrols")

def setup_main_menu(site,ui,profile,m): 
    m = m.add_menu("patrols",MODULE_LABEL)
    m.add_action(Areas)
    m.add_action(Teams)
    m.add_action(Patrols)
