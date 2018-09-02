.. _how_to_use:

===========================
How to use this project
===========================

There are two main resources in this project:  

1. The content of this documentation website  
2. The source code and configuration files in the
   `GitHub repo <https://github.com/jennirinker/code-for-the-world>`_

**Website content**
   
The content of the website is intentionally sparse, and it is oriented
towards practical use. I try not to include too much background information
on the packages I use because that can be found in other places on the
internet. Instead, I've focused on step-by-step guides for you to quickly get
a set-up like the one I use here running for one of your own projects.

There are three sections on the website. First, there is some background
information on how to structure your repo, sphinx, pytest, and setting up
continuous integration with Travis CI. Second, there is some demo pages for
what you might actually have on a real documentation website. Third, there are
some demo examples generated using the ``mypack`` package in the source code
on GitHub.

**Source code on GitHub**

The GitHub repository demonstrates several useful features may be interesting
for you to see a working example:  

1. How Python files can be ordered into a package (see the ``mypack/``
   directory) 
2. A ``setup.py`` file for installing said Python package  
3. A sphinx configuration file that utilizes (``docs/conf.py``)...

   a. The ``autodoc`` extension to scrape information from docstrings
   b. The ``numpydoc`` extension to allow NumPy-style docstrings
   c. The sphinx "Read the Docs" theme

4. Example source files for sphinx documentation that demonstrate
   (``docs/source/``)...

   a. A static webpage
   b. A webpage with content scraped from function/module docstrings
   c. A webpage with examples, featuring code, generated images, and output

5. A directory of tests for checking that the code runs as expected
   (``tests/``)
6. Commands in a Travis CI configuration file to (``.travis.yml``)...

   a. Automatically run ``pytest`` to check the examples work
   b. Automatically run ``pytest`` to run all tests and check the coverage
   c. Use sphinx to build the html pages and then deploy them to GitHub pages
