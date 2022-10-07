# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'By-law'
copyright = '2022, JNO Works Group'
author = 'JNO Works Group'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.
language = 'zh_TW'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = f'<p align="center">聯合現在章程</p>'

html_static_path = ['_static']

html_theme_options = {
    'light_logo': 'JNO-Work-Group.svg',
    'dark_logo': 'JNO-Work-Group_dark.svg',
    'navigation_with_keys': True,
}
# Output file base name for HTML help builder.
htmlhelp_basename = 'JNO Work Group doc'

html_use_smartypants = True

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False
