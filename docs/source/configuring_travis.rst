.. _configuring_travis:

===========================
Configuring Travis CI
===========================

Continuous integration is an extremely powerful tool for automating the testing
and documentation generation of code. You can even hook it up with GitHub pages
to put your documentation on the website.

Configuration steps:

1. Activate Travis CI on a GitHub repository you have owner permissions for.
   Instructions `here <https://docs.travis-ci.com/user/getting-started/>`__.

2. Add the configuration file for Travis CI: ``.travis.yml``. You can use the
   one in this repository as a demo of what you can do with Travis.

3. If you want to push your sphinx documentation to GitHub pages, you need to
   create a personal access token.
