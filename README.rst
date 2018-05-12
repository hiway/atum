atum
====

Atum is a tiny Python library that you can use to emulate the basic
functionality of Erlang’s ``atom`` in your Python scripts.

**Status: Alpha; this is an experiment.**

Erlang documentation:
~~~~~~~~~~~~~~~~~~~~~

   .. rubric:: 3.3 Atom
      :name: atom

   An atom is a literal, a constant with name. An atom is to be enclosed
   in single quotes (’) if it does not begin with a lower-case letter or
   if it contains other characters than alphanumeric characters,
   underscore (_), or @. Examples:

   ::

      hello
      phone_number
      'Monday'
      'phone number'

   http://erlang.org/doc/reference_manual/data_types.html

Unlike Erlang’s atom, ``atum`` does not impose the same limitations. You
may import any valid Python name from atum - even all uppercase.

Install
-------

::

   $ pip install atum

Examples
--------

Instead of writing:

.. code:: python

   @app.route('/register', methods=['GET', 'POST'])
   def register():
       pass

You could write:

.. code:: python

   from atum import GET, POST

   @app.route('/register', methods=[GET, POST])
   def register():
       pass

This might be useful if you use autocompletion. Another benefit is
exceptions occur sooner in case of typos, since the interpreter itself
validates the imported names. Pay attention when importing, simply
tab-to-complete later.

You can compare an atum with another atum or a string.

.. code:: python

   from atum import machine, human

   assert human == human
   assert machine == machine
   assert machine == 'machine'
   assert human != machine 
   assert human is human
   assert machine is machine

Atums also make for readable sentinel values or event-names.

.. code:: python

   from atum import user_is_awake
   from queue import Queue

   q = Queue()

   q.put(user_is_awake)

   assert q.get() == user_is_awake

Technical Details
~~~~~~~~~~~~~~~~~

Atum simply imports Python strings with the same content as their name.

Here is the content of atum.py in its entirety:

.. code:: python

   import sys as _sys

   # intern() is a builtin in Python 2.
   if _sys.version_info > (3, 0):
       intern = _sys.intern


   class Atum(object):
       def __getattr__(self, item):
           if item.startswith('__'):
               return self.__getattribute__(item)
           return intern(item)

       def __getitem__(self, item):
           return item


   _sys.modules[__name__] = Atum()

Known Issues
~~~~~~~~~~~~

-  Atum does not support using ``@`` in imported names as Python’s
   syntax does not allow it.
