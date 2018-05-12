import sys as _sys


class Atum(object):
    def __getattr__(self, item):
        if item.startswith('__'):
            return self.__getattribute__(item)
        return _sys.intern(item)

    def __getitem__(self, item):
        return item


_sys.modules[__name__] = Atum()