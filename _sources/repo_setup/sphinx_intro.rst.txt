.. _sphinx_intro:

===========================
Introduction to sphinx
===========================

Sphinx is a Python package that converts user-created source text files into
some sort of desirable output, often html files that can be hosted on a server
and thus turned into a navigable website. These text files can either be static
content written by the developer (e.g., an installation guide or contributer
guide), but sphinx has several extensions that allow it to automatically
create content from the docstrings of your modules, functions, and classes.
There are special sphinx commands to be inserted into the source text files
in order to trigger this automated sphinx behavior.

The easiest way to get started with sphinx in your project is to use the
``sphinx-quickstart`` command. If you have installed sphinx in your terminal,
then you can run this command. The quickstart walks you through some 
configuration questions, then it will create a docs directory with makefiles
for both Windows and Linux (if you specified that you want a Windows makefile),
and a subdirectory that contains the a sphinx configuration file and the source
text files.

I personally hate the sphinx default style. It uses a theme called alabaster
that I find very visually unappealing. So I often include 
``sphinx_rtd_theme``, which is the sphinx "Read the Docs" theme, as a package
dependency, and I change my ``conf.py`` to use the Read the Docs theme. I also
prefer numpy-style docstrings, so I use the ``numpydoc`` extension. Lastly,
I also use the ``autodoc`` extension to pull content from my docstrings.

If you want to use the same configuration as I do, use the sphinx quickstart 
to generate your ``conf.py``, then use the compare plugin in Notepadd++ to
see which lines are different. Update the ones for you that aren't specific to
your package.

To update the content of your source files, I recommend you check the source
files that I used to generate this very page
`on GitHub <https://github.com/jennirinker/code-for-the-world/tree/master/docs/source>`__.
They will give you an idea of what your text files need to look like in order
to generate a website that looks like this.

Finally, if you want to generate the html files locally and look at what you
website will look like, here is the command (from your docs folder)::

   make html

Your html files are now in the corresponding subdirectory in your build
directory. Double-click ``index.html`` to view the main page. You can set up
Travis CI to automatically generate your documentation and push it to sphinx:
:ref:`configuring_travis`.
