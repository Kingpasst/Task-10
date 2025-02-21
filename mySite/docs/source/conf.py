# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

# Add your Django project root to the path
sys.path.insert(0, os.path.abspath('../..'))

# Setup Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mySite.settings'
django.setup()

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxcontrib_django',
]

# Theme settings
html_theme = 'sphinx_rtd_theme'

# Project information
project = 'NeedWeed'
copyright = '2025, Sihle'
author = 'Sihle'
release = '0.0.0.1'

# Other settings
templates_path = ['_templates']
exclude_patterns = []