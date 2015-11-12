===============
 Building Docs
===============

- ``sphinx-build``
- only modified files are updated [*]_

.. toctree::
    :maxdepth: 1
    
    html_output
    pdf_output

.. [*]  The definition of "modified" depends on the contents of the file.  Include directives seem to always cause a rebuild of the node.
