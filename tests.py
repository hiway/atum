def test_atum():
    from atum import this, that
    assert this != that
    assert this == this
    assert that == that
    assert that is that
    assert that is that


def test_atum_in_queue():
    from atum import user_is_awake
    from queue import Queue
    q = Queue()
    q.put(user_is_awake)
    assert q.get() == user_is_awake


def test_atum_str():
    from atum import user_is_asleep
    assert str(user_is_asleep) == 'user_is_asleep'


def test_atum_repr():
    from atum import online
    assert repr(online) == 'Atum(online)'


def test_atum_import_bare_class_identity_fails():
    from atum import Atum
    from atum import test as test_
    test = Atum('test')
    assert test == test_
    assert test is not test_


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
