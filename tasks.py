from atelier.invlib import setup_from_tasks
ns = setup_from_tasks(
    globals(), "lino_patrols",
    revision_control_system='git',
    tolerate_sphinx_warnings=False,
    blogref_url='http://luc.lino-framework.org',
    cleanable_files=['docs/api/lino_patrols.*'],
    demo_projects=['.'])
