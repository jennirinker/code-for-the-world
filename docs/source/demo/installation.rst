.. _installation:

===========================
Installation
===========================

You should always have installation instructions for your package. Experienced
coders will know how to install your code, but what about new users who may not
be very familiar with Python?

The source files in the
`GitHub repo <https://github.com/jennirinker/code-for-the-world>`__ include a
demo Python package called ``mypack``.
The ``mypack`` package is very simple and all the dependencies are on PyPi.
This means they can all be listed within the ``setup.py`` file. There are three
ways you can install ``mypack``:

1. Directly from the GitHub repository::

    pip install git+https://github.com/jennirinker/code-for-the-world

2. Clone it and then install from the local copy::

    git clone https://github.com/jennirinker/code-for-the-world
    cd code-for-the-world
    pip install .

3. Same as above but with an editable installation good for developers::

    git clone https://github.com/jennirinker/code-for-the-world
    cd code-for-the-world
    pip install -e .
