.. _package_structure:

============================
Structuring your repository
============================

There are four main considerations when building your repository. First, you
need to consider the structure of the package itself. Second, the location of
your tests. Third, the location of the source files for your documentation.
Fourth and last, the location of any examples you provide to your users.

**Structure of a python package**

There are many tutorials online about the structuring of Python packages. You
know, directories with ``*.py`` files and an ``__init__.py`` file,
which tells Python that the directory itself is a module. I won't reinvent the
wheel here; just Google "structure of a Python package" to read more about
that.

An interesting note is the difference between the structure of a package and
it's architecture. In other words, what is the logic behind which functions go
where? DO you put classes in one module? Functions in another? Do you have a
``utils`` folder for basic underlying functionality? I don't know if is a
good answer to this question. It's up to you.


**Where to put tests**

The recommended practice for pytest is
`here <https://docs.pytest.org/en/latest/goodpractices.html>`_.
There are two possible places to put your test files so that pytest can find
them. I prefer placing my tests in a separate directory away from the code.

**Where to put documentation**

The general rule of thumb is to have a top-level directory called ``doc`` or
``docs``. If you run ``sphinx-quickstart`` to initialize your sphinx
documentation, you will run it from the top level of your repository and it
will create this folder for you.

Within your ``docs`` folder, there will be your sphinx configuration file
``conf.py``, the makefiles for converting your source text files into html or
a LaTeX pdf, and a directory with the source files for your documentation,
usually called ``source``. If you have generated the sphinx html files locally,
there will also be a directory with the build files, often called ``build``.

**Where to put examples**

There is no recommended practice for where to store examples or demos for your
code. I like to have a separate folder called ``examples``. Then I can run
``pytest`` on that directory and make sure that my examples all work every time
I update the master branch.
