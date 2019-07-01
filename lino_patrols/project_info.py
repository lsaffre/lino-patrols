# -*- coding: UTF-8 -*-
## Copyright 2013-2016 Luc Saffre
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

SETUP_INFO = dict(name='lino-patrols',
      version='0.0.3', 
      install_requires=['lino'],
      test_suite = 'tests',
      description="A Lino application for managing patrols",
      long_description="""\
Lino-Patrols is a `Lino <http://www.lino-framework.org>`_ 
application for managing and planning patrols.

"A patrol is commonly a group of personnel, such as police officers or
soldiers, that are assigned to monitor a specific geographic area." 
(`Wikipedia <http://en.wikipedia.org/wiki/Patrol>`__)
""",
      author = 'Luc Saffre',
      author_email = 'luc.saffre@gmail.com',
      url="http://patrols.lino-framework.org",
      license='BSD-2-Clause',
      classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2
Development Status :: 1 - Planning
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: GNU General Public License (GPL)
Operating System :: OS Independent
Topic :: Office/Business :: Scheduling
""".splitlines())

SETUP_INFO.update(packages=[
  'lino_patrols',
  'lino_patrols.demo',
  'lino_patrols.patrols',
  'lino_patrols.patrols.fixtures',
  'lino_patrols.settings',
  'lino_patrols.tests',
])

SETUP_INFO.update(message_extractors = {
    'lino_patrols': [
        ('**/cache/**',          'ignore', None),
        ('**.py',                'python', None),
        ('**.js',                'javascript', None),
        ('**/templates_jinja/**.html', 'jinja2', None),
    ],
})

SETUP_INFO.update(package_data=dict())
def add_package_data(package,*patterns):
    l = SETUP_INFO['package_data'].setdefault(package,[])
    l.extend(patterns)
    return l

add_package_data('lino_patrols',
  'config/patrols/Patrol/*.odt',
  'config/patrols/Overview/*.odt')

l = add_package_data('lino_patrols')
for lng in 'fr de nl'.split():
    l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
    

