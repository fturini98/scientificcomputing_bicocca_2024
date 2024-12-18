Documentation
=====================================

An additional feature that I added to this package is the documentation.  
The documentation is generated with **sphinx** to make it more easily accessible.

First Initialization
--------------------

To use **sphinx**, it is necessary to install it with:

.. code-block:: bash

    pip install sphinx

If you want to use the "Read the Docs" theme, it is also necessary to install it:

.. code-block:: bash

    pip install sphinx-rtd-theme

After that, in the main folder of the project, create the **doc** folder with:

.. code-block:: bash

    sphinx-quickstart

- **Note**:  
  Choose the option **NO** for the *Separate source and build directories* question.

This generates the necessary files to make Sphinx work properly.

Modify the conf.py File
~~~~~~~~~~~~~~~~~~~~~~~

It is possible to modify some Sphinx configurations in the `conf.py <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/Esercizi/BicoccaCoursePython2024/docs/conf.py>`_ file to activate several features:

- For the "Read the Docs" theme:

  .. code-block:: python

       html_theme = 'sphinx_rtd_theme'

- For the autodoc extension:

  .. code-block:: python

    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.napoleon',
    ]

- To ensure that Sphinx finds the right folder:

  .. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../src'))  # Add the main project directory to the path

- To add the link to the source code:

  .. code-block:: python

    extensions = [
        'sphinx.ext.viewcode',
    ]

- To have the jupyter notebook included in the documentation via toctree:
  
  - install `Pandoc <https://pandoc.org>`_

  - install with pip the nbsphinx extension:

    .. code-block:: python

      pip install nbsphinx

  - Add the sphinx extension to the conf.py file:

    .. code-block:: python

        extensions = [
        'nbsphinx', # For including jupyter notebook
        ]

        nbsphinx_execute = 'never'

        nbsphinx_allow_errors = True
  
  .. note::

      To make the nbsphinx extension work properly, you must create a symbolic link
      inside the docs folder for the jupyter notebook.
      In the case of the GitHub workflow I manage it by adding a **ln -s** command in the yml file. While for
      building it locally the standard `make.bat <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/Esercizi/BicoccaCoursePython2024/docs/make.bat>`_ file was modified
        

- To add the GitHub button in the html page:

  .. code-block:: python

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

Generate the Restructured Text File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sphinx uses ***rst*** files to generate the documentation.  
To generate an rst file for each module for the first time, simply run:

.. code-block:: bash

    sphinx-apidoc -o docs -F --separate <src/package_name folder>

Build the HTML Pages
~~~~~~~~~~~~~~~~~~~~

To build the actual HTML pages, run the following commands in the *doc* folder:

- For Linux:

  .. code-block:: bash

    ./make html

- For Windows:

  .. code-block:: bash

    ./make.bat html

If had already build the documentation, and you want to generate a new documentation, is usefull to clean up the buil by:

  .. code-block:: bash

    ./make.bat clean

this is because some times sphinx dosen't create the new build for the pages that are not modified and this could generate some problems with the index.

Documentation with Continuous Integration
-----------------------------------------

Because files change with every commit, it is useful to build the documentation through continuous integration.  
This is done using the `BuildDocumentation workflow <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/.github/workflows/BuildDocumentation.yml>`_.  

This workflow builds the documentation for each deployed version of the package and makes it available on the **GitHub Pages** of the repository.

.. note:: To activate the URL for the pages, go to the GitHub's settings under "Pages" and select the branch responsible for the documentation.

After that, the documentation will be available at:

.. code-block:: bash
  
   https://<GitHub-user>.github.io/<GitHub-repository-name>

Badges
------

You can display badges in the `README.md <https://github.com/fturini98/scientificcomputing_bicocca_2024/tree/deployment/Esercizi/BicoccaCoursePython2024/README.md>`_ file for the documentation and the status of individual workflows.  
Badges can be personalized as follows:

- **Choose the branch to check the workflow status** by adding to the URL:

  .. code-block:: bash

    ?branch=<branch name>

- **Choose the label of the badge**:

  .. code-block:: bash

    ?label=<branch name>

.. note:: Spaces in the URL are replaced with **%20**.
