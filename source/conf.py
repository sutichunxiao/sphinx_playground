# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys, os

sys.path.append(os.path.abspath('_ext'))




project = 'guidelines'
copyright = '2023, Su'
author = 'Su'
release = 'V1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'todo',
    # 'sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    # "sphinx.ext.napoleon",
    # "sphinx.ext.todo",'

]

todo_include_todos = True

templates_path = ['_templates']
exclude_patterns = []

# app.add_css_file('css/custom.css')


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
