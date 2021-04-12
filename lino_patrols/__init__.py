# -*- coding: UTF-8 -*-
# Copyright 2013-2016 Summa & Ko Ltd
# License: GNU Affero General Public License v3 (see file COPYING for details)

from os.path import join, dirname

from .setup_info import SETUP_INFO

# above line is equivalent to "execfile(filename)", except that it
# works also in Python 3

# execfile(os.path.join(os.path.dirname(__file__), 'project_info.py'))
__version__ = SETUP_INFO['version']

# intersphinx_urls = dict(docs="https://patrols.lino-framework.org")
# srcref_url = 'https://github.com/lsaffre/lino-patrols/blob/master/%s'
doc_trees = []
