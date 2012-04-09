Snippets
========

.. image:: https://secure.travis-ci.org/trilan/snippets.png?branch=develop

Snippets is a code snippets static repository generator. It is like
Jekyll/Pelican/etc. for blog, but for code snippets.

* Write code snippets with your favorite editor in plain text.
* Moderate incoming snippets using pull requests and awesome GitHub's code
  review features.
* Generate site using only one command.
* Highlight code with `Pygments`_.
* Theme site with `Jinja2`_.

Usage
-----

1. Create directory with code snippets. For example::

       ./snippets/
         example.py
         example.js

   And ``example.py`` is like::

       # !title: How to print `Hello, World!` in Python
       # !date: 2012-04-01
       # !tags: Python, hello

       print 'Hello, World!'

   When ``example.js`` is like::

       /*
        * !title: How to print `Hello, World!` in JavaScript
        * !date: 2012-04-01
        * !tags: JavaScript, hello
        */

       console.log("Hello, World!");

   In header comments you can write some metadata to use it in templates. Every
   metadata param must begin with bang (``!``) and must contain key and value.
   All metadata are optional, except ``title`` and ``date``.

2. Create a theme for your site. Theme is a directory with three Jinja
   templates:

   * ``index.html``;
   * ``snippet.html``;
   * ``tag.html``.

4. Run ``snippets`` command for this directory::

       $ snippets -s snippets -o output -t theme

5. Open ``output/index.html`` in your browser or deploy whole ``output``
   directory to the remote server.

Example
-------

See example repository `here`_.

Contributing
------------

Feel free to fork, send pull requests or report bugs and issues on github.


.. _Pygments: http://pygments.org/
.. _Jinja2: http://jinja.pocoo.org/
.. _here: https://github.com/trilan/snippets.trilandev.com
