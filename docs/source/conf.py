# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Robotics 101'
copyright = '2025, Witty Wizard'
author = 'Witty Wizard'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "_static/logo.png"
html_css_files = ["custom.css"]

# -- Github button -----------------------------------------------------------

html_theme_options = {
    "style_external_links": True,  # Adds an external link icon
    "navigation_depth": 4,
    "prev_next_buttons_location": "bottom",
    "collapse_navigation": False,
    "sticky_navigation": True,
}

html_context = {
    "display_github": True,
    "github_user": "Robotics-PEC",
    "github_repo": "Getting-Started-With-Robotics",
    "github_version": "main",
    "conf_py_path": "/docs/",  # Adjust based on repo structure
}