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



#~ class Employee(dd.Human,dd.Born):
class Employee(contacts.Person,dd.Born):
    def get_workday(self,base,offset=0):
        if base is None: 
            return None
        if offset:
            base += datetime.timedelta(days=offset)
        try:
            return WorkDay.objects.get(date=base,employee=self)
        except WorkDay.DoesNotExist:
            return None
    

class Employees(dd.Table):
    model = Employee
    column_names = "last_name first_name birth_date"
    detail_layout = """
    id first_name last_name gender birth_date
    WorkDaysByEmployee
    """
    
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
    

class PatrolStates(dd.ChoiceList):
    verbose_name = _("PatrolS tate")
    verbose_name_plural = _("Patrol States")
    
add = PatrolStates.add_item
add('10', _("Scheduled"),'scheduled')    
add('20', _("Pending"),'pending')
add('90', _("Done"),'done')

    
class Patrol(dd.Model):
    
    class Meta:
        verbose_name = _("Patrol") 
        verbose_name_plural = _("Patrols") 
    
    date = models.DateField(verbose_name=_("Date"))
    area = models.ForeignKey(Area)
    team = models.ForeignKey(Team)
    remark = models.TextField(blank=True)
    state = PatrolStates.field(default=PatrolStates.scheduled)
    
class Patrols(dd.Table):
    model = Patrol
    parameters = dict(
      dates_from = models.DateField(verbose_name=_("Dates from"),null=True,blank=True),
      dates_until = models.DateField(verbose_name=_("until"),null=True,blank=True),
    )
    column_names = "date area team state"

    detail_layout = """
    date area team state
    remark
    ManningsByPatrol
    """
    
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
    
    
class Manning(dd.Model):
    class Meta:
        verbose_name = _("Manning") 
        verbose_name_plural = _("Mannings") 
    patrol = models.ForeignKey(Patrol)
    employee = models.ForeignKey(Employee)
    
    
class Mannings(dd.Table):
    model = Manning
    
class ManningsByPatrol(Mannings):
    master_key = 'patrol'    
    
#~ class ManningsByEmployee(Mannings):
    #~ master_key = 'employee'    
    

if False:
        
    class Day(dd.Model):
        
        class Meta:
            verbose_name = _("Day") 
            verbose_name_plural = _("Days") 
        
        date = models.DateField(verbose_name=_("Date"),unique=True)
        
    class Days(dd.Table):
        model = Day
    
class WorkDayTypes(dd.ChoiceList):
    verbose_name = _("WorkDay Type")
    verbose_name_plural = _("WorkDay Types")
    
add = WorkDayTypes.add_item
add('10', _("Workday"),'workday')     # Travail / Arbeit
add('20', _("Holiday"),'holiday')     # Férié / Feiertag
add('30', _("Leave day"),'leave')   # Congé / Urlaub
add('40', _("Sick"),'sick')         # Malade / Krank
add('50', _("Absent"),'absent')      # Absent / Abwesend
    
class WorkDay(dd.Model):
    
    class Meta:
        verbose_name = _("Day") 
        verbose_name_plural = _("Days") 
        unique_together = ['date','employee']
    
    date = models.DateField(verbose_name=_("Date"))
    type = WorkDayTypes.field() 
    employee = models.ForeignKey(Employee)
    #~ patrol = models.ForeignKey(Patrol,blank=True,null=True)
    
    #~ def full_clean(self):
        #~ super(WorkDay,self).full_clean()
        #~ if self.type == WorkDayTypes.workday:
            #~ if not self.patrol:
                #~ raise ValidationError("Workday without Patrol")
                
    def __unicode__(self):
        return unicode(self.type)
    
class WorkDays(dd.Table):
    model = WorkDay
    help_text = _("One entry per employee and date.")
    detail_layout = """
    date employee type
    """
    
def first_day_of_week(d):
    if d is None: return None
    if d.weekday() == 0: return d
    return d + datetime.timedelta(days=-d.weekday())
    
class WorkDaysByEmployee(WorkDays):
    master_key = 'employee'
    
    
class EmployeesByWeek(Employees):
    label = _("Employees by Week")
    parameters = dict(
        week=models.DateField(verbose_name=_("Week")),
        dummy = models.BooleanField(verbose_name=_("Dummy")),
        )
    #~ column_names = "last_name first_name mon tue wed thu fri sat sun"
    column_names = "last_name first_name mon tue wed"
    auto_fit_column_widths = True
    
    @classmethod
    def param_defaults(self,ar,**kw):
        kw = super(EmployeesByWeek,self).param_defaults(ar,**kw)
        kw.update(week=first_day_of_week(datetime.date.today()))
        return kw
    
    
    @dd.virtualfield(models.ForeignKey(WorkDay,verbose_name="Mon"))
    def mon(self,obj,ar=None):
        return obj.get_workday(first_day_of_week(ar.param_values.week))
        
    @dd.virtualfield(models.ForeignKey(WorkDay,verbose_name="Tue"))
    def tue(self,obj,ar=None):
        return obj.get_workday(first_day_of_week(ar.param_values.week),1)
        
    @dd.virtualfield(models.ForeignKey(WorkDay,verbose_name="Wed"))
    def wed(self,obj,ar=None):
        return obj.get_workday(first_day_of_week(ar.param_values.week),2)



MODULE_LABEL = _("Patrols")

def setup_explorer_menu(site,ui,profile,m): 
    m = m.add_menu("patrols",MODULE_LABEL)
    m.add_action(WorkDayTypes)
    m.add_action(WorkDays)

def setup_main_menu(site,ui,profile,m): 
    m = m.add_menu("patrols",MODULE_LABEL)
    m.add_action(Areas)
    m.add_action(Employees)
    m.add_action(EmployeesByWeek)
    m.add_action(Teams)
    m.add_action(Patrols)
    m.add_action(Mannings)
    #~ m.add_action(Days)
