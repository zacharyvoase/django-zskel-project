# Zack’s Skeleton Django Project

This is a small skeleton project based on the principles described in my blog
post, “[Django Project Conventions, Revisited][blog post]”.


## Features

*   Designed to work with [virtualenv][venv] and [pip][pip] from the start.

  [venv]: http://pypi.python.org/pypi/virtualenv
  [pip]: http://pip.openplans.org/

*   [Django Debug Toolbar][] installed as standard.

  [django debug toolbar]: http://github.com/robhudson/django-debug-toolbar

*   Logging set up with sensible defaults as standard.

*   Clean implementation of ‘settings modes’; have a single ‘common’ settings
    module, with several deployment-specific settings, all under version
    control. This extends to flat-file configurations too (via the `etcs/`
    directory).

*   Clear separation of immutable/mutable aspects of deployment, with a
    distinction between the *site* and *project* directories. No more large VCS
    ignore files!

*   Compatible with virtually any VCS, and most deployment strategy. Comes with
    VCS ignore files for [Mercurial][] and [Git][].

  [mercurial]: http://mercurial.selenic.com/
  [git]: http://git-scm.com/


## Installation

1.  Make, enter and activate a virtualenv:

        $ virtualenv mysite
        New python executable in mysite/bin/python
        Installing setuptools............done.
        $ cd mysite/
        $ . bin/activate

2.  Clone this repo into a sub-directory of the new virtualenv:

        $ git clone 'git://github.com/zacharyvoase/django-zskel-project.git' myproject
        $ cd myproject/

        # Remove .empty files, used to make Hg track otherwise-empty dirs.
        $ find . -name '.empty' -exec rm {} \;

        $ rm .hgignore # OR
        $ rm .gitignore

3.  Remove the pointer to the GitHub project:

        $ git config --unset remote.origin.url

    Later you’ll probably want to re-add this configuration with a pointer to
    your upstream repo. You can do that with the following command (mutatis
    mutandem):

        $ git config remote.origin.url 'git@github.com:USERNAME/PROJECT.git'

4.  Go through the following files, editing as necessary:

    *   `settings/common.py`
    *   `settings/development.py`
    *   `urls.py`
    *   `REQUIREMENTS`
    *   `templates/base.html`

5.  Symlink the project directory into the virtualenv’s `site-packages`:

        $ ln -s `pwd` ../lib/python2.6/site-packages/`basename pwd`

    Replace `python2.6` with the installed version of Python on your machine.

6.  Set the `DJANGO_SETTINGS_MODULE` environment variable now, and on every
    virtualenv activation:

        $ export DJANGO_SETTINGS_MODULE=myproject.settings.development
        $ echo "!!" >> ../bin/activate

7.  Install the basic project requirements:

        $ easy_install pip
        $ pip install -r REQUIREMENTS

    As you edit your `REQUIREMENTS` file, you can run that last command again;
    `pip` will realise which packages you’ve added and will ignore those already
    installed.


## Managing Your Site

There is no `manage.py` file here; use [django-boss][django-boss] or
`django-admin.py` (which will be on your path after you install Django):

    $ django-admin.py syncdb
    $ django-admin.py runserver
    $ django-admin.py test myapp

  [django-boss]: http://github.com/zacharyvoase/django-boss


## More Information

This layout is based on my original [blog post][]; read that for comprehensive
information on the architecture and rationale behind this project. You can use
the GitHub [issue tracker][] to report bugs or make suggestions.

  [blog post]: http://blog.zacharyvoase.com/2010-02-03-django-project-conventions-revisited
  [issue tracker]: http://github.com/zacharyvoase/django-zskel-project/issues
