.. _contributing:

Contributing
============

Anyone in the community can contribute to this documentation.

The project is hosted at https://github.com/mosen/profiledocs

Submitting an error
===================

If you find that there is an error in the documentation, please raise an issue via `Github Issues <https://github.com/mosen/profiledocs/issues>`_.
Even better, submit a Pull Request for the correction.

Writing Documentation
=====================

The project is generated through sphinx and a plugin called `sphinx-pfmanifest <https://github.com/mosen/sphinx-pfmanifest>`_.

To set up for development:

1. Fork this repo and clone it to your local machine.
2. Install virtualenv if not present
3. Create a virtual environment somewhere and activate it
4. Install requirements (``pip i -r requirements.txt``)
5. Clone and install sphinx-pfmanifest via ``python setup.py install`` in the sphinx-pfmanifest dir.
6. Now you can make changes and run ``make html`` to see the end result.


