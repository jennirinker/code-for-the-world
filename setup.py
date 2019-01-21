# -*- coding: utf-8 -*-
"""Setup file for mypack package

Developer install
-----------------
Run following command in Anaconda prompt/terminal:
    pip install -e .
"""
from setuptools import setup


setup(name='mypack',  # name of package on import
      version='1.0',  # package version
      description='Demo package for teaching packaging',  # brief description
      url='https://github.com/jennirinker/code-for-the-world',  # git repo url
      author='Jenni Rinker',  # author(s)
      author_email='rink@dtu.dk',  # email
      license='MIT',  # licensing
      packages=['mypack',  # main package
                'mypack.utils'],  # utils subdirectory (or use find)
      install_requires=[  # dependencies
        'matplotlib',  # for plotting
        'numpy',  # for numerical calculations
        'numpydoc',  # numpy-style docstrings for sphinx
        'pandas',  # store airfoil data in dataframes
        'pytest>=3.6',  # for testing
        'pytest-cov',  # for calculating coverage
        'sphinx',  # generating documentation
        'sphinx_rtd_theme'  # docs theme
      ],
      zip_safe=True)  # package can be installed from zip file
