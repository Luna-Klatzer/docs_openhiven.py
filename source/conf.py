# -- Project information -----------------------------------------------------

project = 'OpenHiven.py'
copyright = '2020, Nicolas Klatzer'
author = 'Nicolas Klatzer'

# The full version, including alpha/beta/rc tags
release = 'v.0.1b'

# -- General configuration ---------------------------------------------------

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

extensions = ['sphinx-rtd-theme',
            'sphinx.ext.autosectionlabel',
            'sphinx.ext.todo',
            'sphinx.ext.githubpages']

html_theme = 'sphinx-rtd-theme'

html_static_path = ['_static']

html_theme_options = {
    'canonical_url': 'https://openhivenpy.readthedocs.io',
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}