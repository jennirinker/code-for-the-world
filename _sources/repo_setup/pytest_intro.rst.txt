.. _pytest_intro:

===========================
Introduction to pytest
===========================

Code should always be tested. For pure development, tests are set up to check
bugs and make sure that the software has the correct functionality. For
scientific applications, we can also add tests to verify that the model
outputs match the theoretical values.

The process of testing involves writing functions in specific ways and specific
locations and then running special programs on those test modules. The testing
programs will collect the number of failures and return a failure report upon
completion.

There are two main testing packages: ``unittest``, which is built into the
Python library, and ``pytest``, which is a third-party package. The decision of
which of these packages is superior to the other is hotly contested.
Personally, I prefer pytest because I think the tests are easier to understand
for inexperienced programmers. I also like a lot of its functionality, though I
don't know how much of that functionality is duplicated in unittest.

The default behavior for pytest is to iterate through a selected test
directory and to collect all modules titled ``test_*.py``. In each of those
modules, it collects and executes all the functions titled ``test_*``.

This default collection behavior can be overwritten by specifying a special
configuration file. And this is how I get pytest to also test my examples. To
be specific, I create a ``setup.cfg`` file that tells pytest to also collect
modules titled ``example*.py`` and functions titled ``example_*``. The
command to test my examples is then as follows::

   pytest examples/

The last configuration that I really like is a plugin for pytest called
``pytest-cov``, where "cov" stands for "coverage". This plugin allows pytest to
produce a report of what percent of your package is covered by your tests::

   pytest --cov=<package_name> <test_directory>

Unfortunately, due to the way the commands are structured, you cannot check the
examples and check coverage at the same time. This means you need to call pytest
twice, once for examples and once for your tests. But if you set up CI, then all
this means is one more line in your CI configuration file. :)
