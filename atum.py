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
