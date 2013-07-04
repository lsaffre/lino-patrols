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
"""

from __future__ import unicode_literals

import decimal
import datetime
ONE_DAY = datetime.timedelta(days=1)

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _


from lino import dd
from lino.utils import mti
from lino.utils import i2d, Cycler
from lino.utils.instantiator import Instantiator
from lino.core.dbutils import resolve_model
from north.dbutils import babel_values
#~ from north.dbutils import babel_values as babelkw
from north.dbutils import field2kw, babelkw


contacts = dd.resolve_app('contacts')
users = dd.resolve_app('users')
patrols = dd.resolve_app('lino_patrols')
Team = dd.resolve_model('lino_patrols.Team')
Area = dd.resolve_model('lino_patrols.Area')
Employee = dd.resolve_model('lino_patrols.Employee')
Member = dd.resolve_model('lino_patrols.Member')

W = patrols.WorkDayTypes.workday
L = patrols.WorkDayTypes.leave
H = patrols.WorkDayTypes.holiday
S = patrols.WorkDayTypes.sick
WDT = Cycler(
  W,W,W,W,W,L,L,
  S,W,W,W,W,L,L)
  

def objects():
    bd = i2d(19500203)
    for p in contacts.Person.objects.filter(country__isocode="BE"):
        yield mti.insert_child(p,Employee,birth_date=bd)
        bd += datetime.timedelta(days=234) # experimental value

    for i,e in enumerate(Employee.objects.all()):
        if i % 4:
            e.is_chef = True
            e.is_member = False
            yield e
        
    yield Area(name="North")
    yield Area(name="East")
    yield Area(name="South")
    yield Area(name="West")
    
    CHEFS = Cycler(Employee.objects.filter(is_chef=True))
    MEMBERS = Cycler(Employee.objects.filter(is_member=True))
    AREAS = Cycler(patrols.Area.objects.all())
    
    MEMBERS_PER_TEAM = 2
    
    le = list(Employee.objects.filter(is_member=True))
    while len(le) > MEMBERS_PER_TEAM:
        name = '-'.join([o.last_name for o in le[:MEMBERS_PER_TEAM]])
        t = Team(chef=CHEFS.pop(),name=name)
        yield t
        for e in le[:MEMBERS_PER_TEAM]:
            yield Member(team=t,employee=e)
        le = le[MEMBERS_PER_TEAM:]
    
    #~ yield Team(name="One",chef=CHEFS.pop())
    #~ yield Team(name="Two",chef=CHEFS.pop())
    #~ yield Team(name="Three",chef=CHEFS.pop())
    
    TEAMS = Cycler(patrols.Team.objects.all())
    
    d = settings.SITE.demo_date(-20)
    for i in range(50):
        yield patrols.Patrol(date=d,team=TEAMS.pop(),area=AREAS.pop())
        d += ONE_DAY
        
    for p in patrols.Patrol.objects.all():
        yield patrols.WorkDay(date=p.date,employee=p.team.chef,type=WDT.pop())
        for m in p.team.member_set.all():
            yield patrols.WorkDay(date=p.date,employee=m.employee,type=WDT.pop())
            
            
    #~ d = settings.SITE.demo_date(-10)
    #~ for i in range(30):
        #~ for e in Employee.objects.all():
            #~ yield patrols.WorkDay(date=d,employee=e,type=WDT.pop())
        #~ d += ONE_DAY
        #~ WDT.pop()
        
