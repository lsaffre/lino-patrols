"""
Examples how to run these tests::

  $ python setup.py test
  $ python setup.py test -s tests.test_docs
"""

from lino.utils.pythontest import TestCase
from lino_patrols import SETUP_INFO

   
class DemoTests(TestCase):
    """
    $ python setup.py test -s tests.DemoTests.test_admin
    """
    def test_admin(self):
        # self.run_django_admin_test('lino_patrols.settings.demo')
        self.run_django_manage_test('lino_patrols/demo')

class PackagesTests(TestCase):
    def test_packages(self): 
        self.run_packages_test(SETUP_INFO['packages'])

