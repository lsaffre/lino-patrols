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

from os.path import join, dirname

filename = join(dirname(__file__), 'project_info.py')
exec(compile(open(filename, "rb").read(), filename, 'exec'))

# above line is equivalent to "execfile(filename)", except that it
# works also in Python 3

# execfile(os.path.join(os.path.dirname(__file__), 'project_info.py'))
__version__ = SETUP_INFO['version']

intersphinx_urls = dict(docs="http://patrols.lino-framework.org")
srcref_url = 'https://github.com/lsaffre/lino-patrols/blob/master/%s'
