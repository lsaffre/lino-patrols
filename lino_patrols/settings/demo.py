"""
The settings.py used for building both `/docs` and `/userdocs`
"""
from lino_patrols.settings import *

class Site(Site):
  
    title = "Lino-Patrols demo"
  
    #~ languages = ['en']
    languages = 'en fr nl'
    #~ languages = ['de','fr']
    #~ languages = ['fr','de']
    #~ languages = ['de']
    #~ use_jasmine = True
    use_davlink = False
    use_eid_jslib = False
    remote_user_header = None # 20121003
        
SITE = Site(globals())
#~ print 20130409, __file__, LOGGING
