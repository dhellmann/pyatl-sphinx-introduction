===========================
 Input is reStructuredText
===========================

.. index::
    single: reStructuredText

- Simple text markup
- Uses semantic and stylistic tags
- Extensible with Python

  - `Role Quick-reference`_
  - `Directive Quick-reference`_

.. _Role Quick-reference: http://docutils.sf.net/docs/ref/rst/roles.html
.. _Directive Quick-reference: http://docutils.sourceforge.net/docs/ref/rst/directives.html

Inline Markup
=============

*emphasis*; **strong emphasis**; `interpreted text`; `interpreted text
with role`:emphasis:; ``inline literal text``; standalone hyperlink,
http://docutils.sourceforge.net; named reference, reStructuredText_;
`anonymous reference`__; footnote reference, [1]_; citation reference,
[CIT2002]_; |substitution|; _`inline internal target`.

::

   *emphasis*; **strong emphasis**; `interpreted text`; `interpreted text
   with role`:emphasis:; ``inline literal text``; standalone hyperlink,
   http://docutils.sourceforge.net; named reference, reStructuredText_;
   `anonymous reference`__; footnote reference, [1]_; citation reference,
   [CIT2002]_; |substitution|; _`inline internal target`.

Body Elements
=============
Grid table:

+--------------------------------+-----------------------------------+
| Paragraphs are flush-left,     | Literal block, preceded by "::":: |
| separated by blank lines.      |                                   |
|                                |     Indented                      |
|     Block quotes are indented. |                                   |
+--------------------------------+ or::                              |
| >>> print 'Doctest block'      |                                   |
| Doctest block                  | > Quoted                          |
+--------------------------------+-----------------------------------+
| | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
| |     Useful for addresses, verse, and adornment-free lists; long  |
|       lines can be wrapped with continuation lines.                |
+--------------------------------------------------------------------+

::

   +--------------------------------+-----------------------------------+
   | Paragraphs are flush-left,     | Literal block, preceded by "::":: |
   | separated by blank lines.      |                                   |
   |                                |     Indented                      |
   |     Block quotes are indented. |                                   |
   +--------------------------------+ or::                              |
   | >>> print 'Doctest block'      |                                   |
   | Doctest block                  | > Quoted                          |
   +--------------------------------+-----------------------------------+
   | | Line blocks preserve line breaks & indents. [new in 0.3.6]       |
   | |     Useful for addresses, verse, and adornment-free lists; long  |
   |       lines can be wrapped with continuation lines.                |
   +--------------------------------------------------------------------+

Simple tables:

================  ============================================================
List Type         Examples (syntax in the `text source <cheatsheet.txt>`_)
================  ============================================================
Bullet list       * items begin with "-", "+", or "*"
Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
                  #. also auto-enumerated
Definition list   Term is flush-left : optional classifier
                      Definition is indented, no blank line between
Field list        :field name: field body
Option list       -o  at least 2 spaces between option & description
================  ============================================================

::

   ================  ============================================================
   List Type         Examples (syntax in the `text source <cheatsheet.txt>`_)
   ================  ============================================================
   Bullet list       * items begin with "-", "+", or "*"
   Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
                     #. also auto-enumerated
   Definition list   Term is flush-left : optional classifier
                         Definition is indented, no blank line between
   Field list        :field name: field body
   Option list       -o  at least 2 spaces between option & description
   ================  ============================================================


.. _[1]: Footnote goes here
