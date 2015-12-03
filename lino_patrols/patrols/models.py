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

"""
The :xfile:`models` module for :mod:`lino_faggio`.

"""

from __future__ import unicode_literals

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

from lino.api import dd
from lino import mixins

contacts = dd.resolve_app('contacts')
countries = dd.resolve_app('countries')


class Employee(contacts.Person, mixins.Born):
    
    class Meta:
        verbose_name = _("Employee") 
        verbose_name_plural = _("Employees") 
    
    is_member = models.BooleanField(_("Member"),default=True)
    is_chef = models.BooleanField(_("Chef"),default=False)
    #~ member_from = models.DateField(verbose_name=_("Active from"),null=True,blank=True)
    #~ member_until = models.DateField(verbose_name=_("until"),null=True,blank=True)
    
    #~ chef_from = models.DateField(verbose_name=_("Active from"),null=True,blank=True)
    #~ chef_until = models.DateField(verbose_name=_("until"),null=True,blank=True)

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
    is_member is_chef
    MembersByEmployee TeamsByChef WorkDaysByEmployee
    """
    
class Area(mixins.BabelNamed):
    
    class Meta:
        verbose_name = _("Area") 
        verbose_name_plural = _("Areas")
        
class Areas(dd.Table):
    model = Area
    detail_layout = """
    id name 
    PatrolsByArea
    """
    

class Team(mixins.BabelNamed):
    
    class Meta:
        verbose_name = _("Team") 
        verbose_name_plural = _("Teams") 
    
    active_from = models.DateField(verbose_name=_("Active from"),null=True,blank=True)
    active_until = models.DateField(verbose_name=_("until"),null=True,blank=True)
    
    chef = models.ForeignKey(Employee,verbose_name=_("Team leader"))

    @dd.displayfield(_("Team"))
    def info(self, ar):
        if ar is None:
            return ''
        return ar.obj2html(self)
        

class Teams(dd.Table):
    model = Team
    detail_layout = """
    id name 
    active_from active_until chef
    MembersByTeam PatrolsByTeam
    """

class TeamsByChef(Teams):
    label = _("Responsible for")
    master_key = 'chef'
    auto_fit_column_widths = True
    column_names = "info"
    
    
class Member(dd.Model):
    class Meta:
        verbose_name = _("Member") 
        verbose_name_plural = _("Members") 
    #~ patrol = models.ForeignKey(Patrol)
    team = models.ForeignKey(Team)
    employee = models.ForeignKey(Employee)
    
    def __unicode__(self):
        return "%s %s" % (self.employee,self.team)
    
    
class Members(dd.Table):
    help_text = _("A member is when a given employee is part of a given team.")
    model = Member
    
#~ class MembersByPatrol(Members):
    #~ master_key = 'patrol'    
    #~ 
class MembersByTeam(Members):
    master_key = 'team'
    auto_fit_column_widths = True
    
class MembersByEmployee(Members):
    master_key = 'employee'    
    auto_fit_column_widths = True
    label = _("Member of")
    


class PatrolStates(dd.ChoiceList):
    verbose_name = _("Patrol State")
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
    remark = models.TextField(_("Remark"),blank=True)
    state = PatrolStates.field(default=PatrolStates.scheduled.as_callable)
    
    def __unicode__(self):
        return "%s %s %s" % (self.date,self.area,self.team)
    
class Patrols(dd.Table):
    help_text = _("A patrol is when a given team works in a given area on a given day.")
    model = Patrol
    parameters = dict(
      dates_from = models.DateField(verbose_name=_("Dates from"),null=True,blank=True),
      dates_until = models.DateField(verbose_name=_("until"),null=True,blank=True),
    )
    column_names = "date area team state *"
    hidden_columns = 'remark'

    detail_layout = """
    date area team state
    remark
    WorkDaysByPatrol
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
    hidden_columns = 'team remark'
    auto_fit_column_widths = True
    
class PatrolsByArea(Patrols):
    master_key = 'area'    
    hidden_columns = 'area remark'
    auto_fit_column_widths = True
    
    
if False:
    
    class DayTypes(dd.ChoiceList):
        verbose_name = _("Day Type")
        verbose_name_plural = _("Day Types")
        
    add = WorkDayTypes.add_item
    add('10', _("Normal"),'normal')
    add('20', _("Weekend"),'weekend')
    add('30', _("Feast"),'feast')


    class Day(mixins.BabelNamed):
        
        class Meta:
            verbose_name = _("Day") 
            verbose_name_plural = _("Days") 
        
        date = models.DateField(verbose_name=_("Date"),unique=True)
        type = DayTypes.field()
        
    class Days(dd.Table):
        model = Day
        help_text = _("One entry per calendar date.")
    

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
        return "%s %s %s" % (self.date,self.employee,self.type)
    
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
    auto_fit_column_widths = True
    hidden_columns = 'id employee'
    
class WorkDaysByPatrol(WorkDays):
    label = _("Presences")
    master = Patrol
    auto_fit_column_widths = True
    column_names = 'employee type'
    #~ hidden_columns = 'id employee'
    #~ can_create = False
    
    @classmethod
    def get_request_queryset(self,ar):
        #~ logger.info("20121010 Clients.get_request_queryset %s",ar.param_values)
        patrol = ar.master_instance
        if patrol is None: return []
        #~ qs = super(WorkDaysByPatrol,self).get_request_queryset(ar)
        #~ el = [patrol.team.chef] + [m.employee for m in patrol.team.member_set.all()]
        #~ el = [m.employee for m in patrol.team.member_set.all()]
        el = patrol.team.member_set.values_list('employee__id',flat=True)
        #~ return WorkDay.objects.filter(date=patrol.date,employee__in=el)
        return WorkDay.objects.filter(date=patrol.date,employee__id__in=el)
        #~ return qs
            
    
    
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



