# -*- coding: UTF-8 -*-
# Copyright 2013-2016 Luc Saffre
# License: GNU Affero General Public License v3 (see file COPYING for details)

SETUP_INFO = dict(name='lino-patrols',
                  version='0.0.3',
                  install_requires=['lino'],
                  test_suite='tests',
                  description="A Lino Django application for managing patrols",
                  long_description="""\
Lino-Patrols is a `Lino <https://www.lino-framework.org>`_
application for managing and planning patrols.

"A patrol is commonly a group of personnel, such as police officers or
soldiers, that are assigned to monitor a specific geographic area."
(`Wikipedia <https://en.wikipedia.org/wiki/Patrol>`__)
""",
                  author='Luc Saffre',
                  author_email='luc.saffre@gmail.com',
                  url="https://github.com/lsaffre/lino-patrols",
                  license_files=['COPYING'],
                  classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 3
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

SETUP_INFO.update(
    message_extractors={
        'lino_patrols': [
            ('**/cache/**', 'ignore', None),
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates_jinja/**.html', 'jinja2', None),
        ],
    })

SETUP_INFO.update(package_data=dict())


def add_package_data(package, *patterns):
    l = SETUP_INFO['package_data'].setdefault(package, [])
    l.extend(patterns)
    return l


add_package_data('lino_patrols', 'config/patrols/Patrol/*.odt',
                 'config/patrols/Overview/*.odt')

l = add_package_data('lino_patrols')
for lng in 'fr de nl'.split():
    l.append('locale/%s/LC_MESSAGES/*.mo' % lng)
