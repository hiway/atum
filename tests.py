def test_atum():
    from atum import this, that
    assert this != that
    assert this == this
    assert that == that
    assert that is that
    assert that is that


def test_atum_in_queue():
    import sys
    from atum import user_is_awake
    if sys.version_info > (3, 0):
        from queue import Queue
    else:
        from Queue import Queue
    q = Queue()
    q.put(user_is_awake)
    assert q.get() == user_is_awake


def test_atum_str():
    from atum import user_is_asleep
    assert str(user_is_asleep) == 'user_is_asleep'


def test_atum_repr():
    from atum import online
    assert repr(online) == "'online'"


def test_atum_getattr_arbitrary_atoms():
    from atum import test as test_1
    import atum
    test_2 = getattr(atum, 'test')
    assert test_1 == test_2
    assert test_1 is test_2


def test_atum_lookup_items():
    from atum import test as test_1
    import atum
    test_2 = atum['test']
    assert test_1 == test_2
    assert test_1 is test_2


def test_atum_string_compare():
    # https://github.com/hiway/atum/issues/1
    from atum import this_is_a_test
    assert this_is_a_test == 'this_is_a_test'
