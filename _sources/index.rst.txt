.. Code for the World documentation master file, created by
   sphinx-quickstart on Sat Sep  1 14:00:53 2018.

Welcome to Code for the World
=============================

Here are a few scenarios. Do any of them sound familiar? 

* You spend hours and hours writing beautiful Python code that follows all
  PEP conventions and does everything your lab could ever want. You happily
  introduce your repo to your colleagues. Three weeks later, they're still
  not using it. Even worse, they're writing code that duplicates functions
  in your files.  
* You've got a bunch of functions and files and you want to share it with
  your colleagues. But how?  
* You've struggled through learning ``sphinx`` and you've managed to structure
  all the source files so the generated html files look nice. But where can
  you put those files so new people can read them and learn to use your code?
* Your team just did a massive API restructure. After days of work, all your
  tests finally pass again. You drink. Weeks later, someone submits an 
  issue...your examples are all broken.
* You've written a lot of beautiful tests, but you keep forgetting to run them
  every time you make changes to master. Surely there is a better way to do
  this???

I feel your pain. This repo is meant to be an example that you can
reverse-engineer to learn about and implement...

* Package structuring
* Making a documentation website using sphinx and GitLab pages
* Configuring Travis-CI to automate testing and documentation generation

Sound interesting? Cool. Read on: :ref:`how_to_use`.

The source code used to generate the website can be found 
`on GitHub <https://github.com/jennirinker/code-for-the-world>`_.
This project was developed by Jenni Rinker for the 2018 summer school in
`Advanced Scientific Programming in Python <https://python.g-node.org/wiki/>`__
in Camerino, Italy.

Project Contents
=================

.. toctree::
    :maxdepth: 2

    how_to_use

.. toctree::
    :caption: Setting up your repo
    :maxdepth: 2

    repo_setup/repo_structure
    repo_setup/sphinx_intro
    repo_setup/pytest_intro
    repo_setup/configuring_travis

.. toctree::
    :caption: Demo documentation
    :maxdepth: 2

    demo/installation
    demo/api

.. toctree::
    :caption: Demo examples
    :maxdepth: 2

    examples/example_1
    examples/example_2