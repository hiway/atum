# atum

Erlang-like atoms in Python 3

**Status: Alpha; this is an experiment.**

A tiny utility that lets you refer to often-used 
strings in your project as imported object names. 

Instead of writing:

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    pass
```

You could write:

```python
from atum import GET, POST

@app.route('/register', methods=[GET, POST])
def register():
    pass
```

This might be useful if you use autocompletion.
Another benefit is exceptions occur sooner in case of typos,
since the interpreter itself validates the imported names.
Pay attention when importing, simply tab-to-complete later.


## Examples


```python
from atum import machine, human

assert human == human
assert machine == machine
assert human != machine 
assert human is human
assert machine is machine
```


```python
from atum import user_is_awake
from queue import Queue

q = Queue()

q.put(user_is_awake)

assert q.get() == user_is_awake
```
