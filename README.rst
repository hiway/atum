atum
====

Atum is a tiny Python library that you can use to emulate the basic
functionality of Erlang’s ``Atom`` in your Python scripts.

**Status: Alpha; this is an experiment.**

Erlang documentation:
---------------------

http://erlang.org/doc/reference_manual/data_types.html

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

Known Issues
~~~~~~~~~~~~

-  Atum does not support using ``@`` in imported names as Python’s
   syntax does not allow it.
