"""
Examples how to run these tests::

  $ python setup.py test
  $ python setup.py test -s tests.DocsTests
  $ python setup.py test -s tests.DocsTests.test_debts
  $ python setup.py test -s tests.DocsTests.test_docs
"""
from unipath import Path

ROOTDIR = Path(__file__).parent.parent

# load  SETUP_INFO:
execfile(ROOTDIR.child('lino_patrols','setup_info.py'),globals())

from atelier.test import SubProcessTestCase
#~ from djangosite.utils.test import TestCase
"""
Note that we cannot import :mod:`djangosite.utils.test` here
because that's designed for unit tests within a particular Django project 
(run using `djange-admin test`).
"""
from djangosite.utils import testcase_setup


class BaseTestCase(SubProcessTestCase):
#~ class BaseTestCase(TestCase):
    default_environ = dict(DJANGO_SETTINGS_MODULE="lino_patrols.demo.settings")
    project_root = ROOTDIR
    
    def setUp(self):
        #~ settings.SITE.never_build_site_cache = self.never_build_site_cache
        #~ settings.SITE.remote_user_header = 'REMOTE_USER'
        testcase_setup.send(self)
        super(BaseTestCase,self).setUp()
    
    
class DemoTests(BaseTestCase):
    """
    $ python setup.py test -s tests.DemoTests.test_admin
    """
    def test_admin(self): self.run_django_admin_test('lino_patrols.demo.settings')
    


class PackagesTests(BaseTestCase):
    def test_packages(self): self.run_packages_test(SETUP_INFO['packages'])

