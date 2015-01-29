from atelier.fablib import *
setup_from_fabfile(globals(), 'lino_patrols', 'lino_patrols.settings.demo')

add_demo_project('.')

#~ env.demo_database = 'lino_welfare.demo.settings'

#~ env.demo_databases.append('lino_patrols.settings.demo')
#~ env.django_databases.append('userdocs')
# env.tolerate_sphinx_warnings = True

#~ env.languages = 'en fr nl'.split()

env.revision_control_system = 'git'
