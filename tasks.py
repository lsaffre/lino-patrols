from lino.invlib.ns import ns
ns.setup_from_tasks(
    globals(), "lino_patrols",
    revision_control_system='git',
    tolerate_sphinx_warnings=False,
    blogref_url='http://luc.lino-framework.org',
    cleanable_files=['docs/api/lino_patrols.*'],
    demo_projects=['lino_patrols.settings.demo'])
