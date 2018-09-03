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

   a. Go to your `Settings page <https://github.com/settings>`__ on
      GitHub, then click "Developer Settings" then "Personal access tokens".
   
   b. Generate a new token. If the repo is public, you only need to check the
      box related to accessing public repos. You can alternatively check the
      box for all repo settings. **IMPORTANT!!!** Copy this token somewhere
      before you leave the page. You will never be able to see it again.

   c. Go to `travis-ci.com <https://travis-ci.com/>`__ and find the settings for the
      repository you're working on. In the "Environment Variables" section,
      defined a new one called ``GITHUB_TOKEN`` and copy in your token from
      the step above. **IMPORTANT!!!** Be sure that the toggle to display 
      the value in the build log is off. This is a private token that should
      not be shared.  

4. Assuming your Travis CI configuration file and your repo are structured
   properly, this should be it! You can go to
   `travis-ci.com <https://travis-ci.com/>`__ to monitor any running builds. If
   you choose to push to GitLab pages, then the URL for that should be
   ``https://<user>.github.io/<repo_name>``.
