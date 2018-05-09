import sys as _sys

ATUMS = {}


class Atum(object):
    def __init__(self, name):
        self._name = name

    def __eq__(self, other):
        if isinstance(other, str):
            return self._name == other
        return self._name == getattr(other, '_name')

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Atum({})'.format(self._name)


class AtumImportMagic(object):
    def __getattr__(self, item):
        if item.startswith('__'):
            return self.__getattribute__(item)
        if item == 'Atum':
            return Atum
        if item not in ATUMS:
            ATUMS[item] = Atum(name=item)
        return ATUMS[item]

    def __getitem__(self, item):
        return ATUMS[item]


_sys.modules[__name__] = AtumImportMagic()
