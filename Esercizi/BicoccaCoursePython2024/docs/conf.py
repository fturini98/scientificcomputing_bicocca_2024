# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))  # Add the main project directory to the path

# -- Project information -----------------------------------------------------
project = 'BicoccaCoursePython2024'
copyright = '2024, Francesco Turini'
author = 'Francesco Turini'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx', # For including jupyter notebook
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',    # Generates documentation from docstrings
    'sphinx.ext.napoleon',   # Supports Google-style and NumPy-style docstrings
    'sphinx.ext.viewcode',   # Links to the source code of functions
]

nbsphinx_execute = 'never'
nbsphinx_allow_errors = True

autodoc_member_order = 'groupwise'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'style_external_links': True,
}

# -- Add GitHub link in the footer -------------------------------------------
html_context = {
    'display_github': True,  #Show GitHub button
    'github_user': 'fturini98',  # GitHub username
    'github_repo': 'scientificcomputing_bicocca_2024',  # repositoriy name
    'github_version': 'deployment',  # Branch )
    'conf_py_path': '/Esercizi/BicoccaCoursePython2024/docs/',  # Path to doc folder
}