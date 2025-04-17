# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

from sphinx import version_info as sphinx_version

# -- Local Vars --------------------------------------------------------------

# Not used directly by Sphinx, but used by this file and the buildbot.

pinerig_version = "1.0"

# -- Project information -----------------------------------------------------

project = 'Pinerig Documentation'
copyright = '2025, Enip-OIXth'
author = 'Enip-OIXth'

release = '0.1'
version = '0.1.0'

# -- Extension configuration -------------------------------------------------

extensions = [
    '404',
    'icons',
    'reference',
    'sphinx_design',
    'sphinx_inline_tabs',
    'sphinx_copybutton',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "sphinx.ext.mathjax",
    'sphinx.ext.todo',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Is there a better way to check for PDF building?
if "latex" in sys.argv:
    # To convert GIF images when making a PDF.
    extensions.append("sphinx.ext.imgconverter")
    image_converter = "magick"

# A string of reStructuredText that will be included at the end of every
# source file that is read. This is a possible place to add substitutions
# that should be available in every file.
rst_epilog = """
.. |PINERIG_VERSION| replace:: {:s}
.. |TODO| replace:: The documentation here is incomplete`.
""".format(pinerig_version)

# The default language to highlight source code in.
highlight_language = "python3"

# If true, figures, tables and code-blocks are automatically numbered if they have a caption.
numfig = False

# if set to 0, figures, tables and code-blocks are continuously numbered starting at 1.
numfig_secnum_depth = 0

# -- Options for HTML output -------------------------------------------------

# A list of paths that contain custom themes, either as subdirectories
# or as zip files. Relative paths are taken as relative to
# the configuration directory.

html_theme_path = ["build_files/theme"]
html_static_path = []
# Add any paths that contain templates here, relative to this directory.
templates_path = ["build_files/templates"]


# The theme to use for HTML and HTML Help pages.
html_theme = 'furo'

# A dictionary of options that influence the look and feel of
# the selected theme. These are theme-specific.
html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "top_of_page_buttons": [],

    "light_css_variables": {
        "color-foreground-primary": "black",        # for main text and headings
        "color-foreground-secondary": "#5a5c63",    # for secondary text
        "color-foreground-border": "#878787",       # for content borders

        "color-brand-primary": "#265787",
        "color-brand-content": "#265787",
        "color-admonition-background": "purple",
     },

     
    "dark_css_variables": {
         "color-brand-primary": "#265787",
    },

    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/Enip-OIXth/Pinerig-Documentation",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],

    "source_repository": "https://github.com/Enip-OIXth/Pinerig-Documentation/",
    "source_branch": "main",
    "source_directory": "docs/",
}

html_sidebars = {
        "**": [
            "sidebar/brand.html",
            "sidebar/search.html",
            "sidebar/scroll-start.html",
            "sidebar/navigation.html",
            "sidebar/scroll-end.html",
            "sidebar/variant-selector.html",
        ]
}

html_css_files = [
        "css/theme_overrides.css",
        "css/version_switch.css",
        "fonts/bl-icons.css",
    ]

html_js_files = [
        "js/version_switch.js",
    ]

pygments_style = "sphinx"
pygments_dark_style = "monokai"

# If given, this must be the name of an image file
# (path relative to the configuration directory) that is the logo of the docs,
# or URL that points an image file for the logo.
#
# Socket logo from: https://www.blender.org/about/logo
html_logo = "build_files/theme/blender-logo.svg"
html_favicon = "build_files/theme/favicon.png"

# Additional templates that should be rendered to HTML pages,
# must be a dictionary that maps document names to template names.
html_additional_pages = {
    "404": "404.html",
}

# If true, "(C) Copyright …" is shown in the HTML footer.
html_show_copyright = True

# If true, "Created using Sphinx" is shown in the HTML footer.
html_show_sphinx = False

# If true, the text around the keyword is shown as summary of each search result.
html_show_search_summary = True

# If this is not None, a "Last updated on:" timestamp is inserted at
# every page bottom, using the given strftime() format.
# The empty string is equivalent to "%b %d, %Y"
# (or a locale-dependent equivalent).
html_last_updated_fmt = "%Y-%m-%d"

# If true, the reST sources are included in the HTML build as _sources/name.
html_copy_source = False

# If true (and html_copy_source is true as well), links to the reST sources
# will be added to the sidebar.
html_show_sourcelink = False

# -- Options for HTML help output --------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Pinerig Documentation"

# -- Options for EPUB output -------------------------------------------------

# The HTML theme for the epub output. Since the default themes are
# not optimized for small screen space, using the same theme for HTML
# and epub output is usually not wise.
epub_theme = "epub"
epub_description = "Pinerig Documentation"
epub_publisher = "Enip-OIXth"
epub_copyright = "This manual is licensed under a CC-BY-SA 4.0 Int. License."

epub_cover = (
    "_static/cover.png",
    "epub-cover.html",
)

epub_css_files = ["css/epub_overrides.css"]

# A list of files that are generated/copied in the build directory
# but should not be included in the epub file.
epub_exclude_files = ["search.html", "404.html"]

# The depth of the table of contents in the file toc.ncx.
epub_tocdepth = 2

# Control whether to display URL addresses.
epub_show_urls = "no"

# If true, add an index to the epub document.
# epub_use_index = True
