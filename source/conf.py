# -- Project information -----------------------------------------------------

project = 'OpenHiven.py'
copyright = '2020, FrostbyteSpace'
author = 'FrostbyteSpace' #Could use Nicolas Klatzer & Robyn Brittain, but..

# The full version, including alpha/beta/rc tags
release = 'v.0.1b'
version = 'v.0.0.7'

# -- General configuration ---------------------------------------------------

master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = []
templates_path = ['_templates']
exclude_patterns = []

extensions = ['sphinx_rtd_theme',
            'sphinx.ext.autosectionlabel',
            'sphinx.ext.todo',
            'sphinx.ext.githubpages']

pygments_style = 'default'

import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_context = {}
html_logo = "./_static/openhivenpy_white_200x200.png"

html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5,
}


html_theme_options = {
    'canonical_url': 'https://openhivenpy.readthedocs.io',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': 'dark_grey',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_css_files = [
    "stylize.css"
]