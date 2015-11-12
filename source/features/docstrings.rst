========================
 Incorporate docstrings
========================

.. index::
    pair: source; code

.. module:: example
    :synopsis: Simple bit of code to illustrate Sphinx features.

.. moduleauthor:: Doug Hellmann <doug.hellmann@gmail.com>

MyClass
=======

.. autoclass:: MyClass

Methods
-------

.. literalinclude:: example.py
   :lines: 26-29

.. automethod:: MyClass.another_method

.. literalinclude:: example.py
   :lines: 31-39

.. automethod:: MyClass.method_with_arguments



main()
======

.. autofunction:: main
