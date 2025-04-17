Welcome to TESTING GROUNDS!
===================================


|release|
|version|
|today|
|translation progress|

--------------------

.. note::
    An especially important bit of information that the reader should know. The content of the directive should be written in complete sentences and include all appropriate punctuation.
    This project is under active development.
.. tip::
    Some useful tidbit of information for the reader. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. warning::
    An important bit of information that the reader should be very aware of. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. error::
    Information relating to failure modes of some description. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. hint::
    Information that is helpful to the reader. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. important::
    Information that is of paramount importance and which the reader must not ignore. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. caution::
    Information with regard to which the reader should exercise care. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. danger::
    Information which may lead to near and present danger if not heeded. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. attention::
    Information that requires the reader’s attention. 
    The content of the directive should be written in complete sentences and include all appropriate punctuation.
.. seealso::
   Python's :py:mod:`zipfile` module
      Documentation of Python's standard :py:mod:`zipfile` module.

   `GNU tar manual, Basic Tar Format <https://example.org>`_
      Documentation for tar archive files, including GNU tar extensions.

--------------------

.. versionadded:: 2.5
   The *spam* parameter.

--------------------

.. versionchanged:: 2.8
   The *spam* parameter is now of type *boson*.

--------------------

.. deprecated:: 3.1
   Use :py:func:`spam` instead.

--------------------

.. versionremoved:: 4.0
   The :py:func:`spam` function is more flexible, and should be used instead.

--------------------

.. rubric::
    A rubric is like an informal heading that doesn’t correspond to the document’s structure, i.e. it does not create a table of contents node.

--------------------

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

--------------------

Since Pythagoras, we know that :math:`a^2 + b^2 = c^2`.

--------------------

.. function:: foo(x)
              foo(y, z)
   :module: some.module.name

   Return a line of text input from the user.

--------------------

... is installed in :file:`/usr/lib/python3.{x}/site-packages` ...

--------------------

.. role:: python(code)
   :language: python

In Python, :python:`1 + 2` is equal to :python:`3`.

--------------------

.. code-block::
   :caption: A cool example

       The output of this line starts with four spaces.

--------------------

.. code-block::

       The output of this line has no spaces at the beginning.

--------------------

.. dropdown:: Dropdown title

    Dropdown content

--------------------

.. tab-set::

    .. tab-item:: Label1

        Content 1

    .. tab-item:: Label2

        Content 2

--------------------

.. card:: Card Title

    Header
    ^^^
    Card content
    +++
    Footer

--------------------

.. |name| replace:: replacement *text*

--------------------

Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.