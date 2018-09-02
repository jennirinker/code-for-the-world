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

This repo is meant to serve an example that you can reverse-engineer to learn
about and implement...

* Package structuring
* Making a documentation website using sphinx and GitLab pages
* Automated testing using Travis-CI
* Automatic docs generation using Travis-CI

The source code used to generate the website can be found 
`on GitHub <https://github.com/jennirinker/code-for-the-world>`_.
This project was developed for the 2018 Advanced Scientific Python Programming
summer school in Camerino, Italy.

Project Contents
=================

.. toctree::
    :caption: User Guide
    :maxdepth: 2

    installation
    configuring_travis
    api

.. toctree::
    :caption: Examples
    :maxdepth: 2

    examples/example_1
    examples/example_2