# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Pinerig Documentation'
copyright = '2025, Enip-OIXth'
author = 'Enip-OIXth'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False, # Only display the logo image, do not display the project name at the top of the sidebar
    'prev_next_buttons_location': 'bottom', # Location to display Next and Previous buttons. This can be either bottom, top, both , or None.
    'style_external_links': False, # Add an icon next to external links.
    'vcs_pageview_mode': '', # Changes how to view files when using display_github, display_gitlab, etc. When using GitHub or GitLab this can be: blob (default), edit, or raw. On Bitbucket, this can be either: view (default) or edit.
    'style_nav_header_background': '#29b962', # Changes the background of the search area in the navigation bar. The value can be anything valid in a CSS background property (default : #2980B9).
    'flyout_display': 'hidden', # Specify how to display the flyout (language and version selector). This can be either attached or hidden. attached means that it will show the flyout in the bottom of the sidebar. You will need to disable the default Read the Docs flyout in order to not have 2 flyouts showing.
    'version_selector': True, # Display a version selector below the title. This feature makes usage of Read the Docs Addons for this, so it’s required the documentation to be hosted on Read the Docs. It only appears when there are more than 1 active version.
    'language_selector': True, # Display a language selector below the title. This feature makes usage of Read the Docs Addons for this, so it’s required the documentation to be served on Read the Docs. It only appears when there is more than 1 active language.
    # Toc options
    'collapse_navigation': True, # With this enabled, navigation entries are not expandable – the [+] icons next to each entry are removed.
    'sticky_navigation': True, # Scroll the navigation with the main page content as you scroll the page.
    'navigation_depth': 4, # The maximum depth of the table of contents tree. Set this to -1 to allow unlimited depth.
    'includehidden': True, # Specifies if the navigation includes hidden table(s) of contents – that is, any toctree directive that is marked with the :hidden: option.
    'titles_only': False, # When enabled, page subheadings are not included in the navigation.
}


# -- Options for EPUB output
epub_show_urls = 'footnote'
