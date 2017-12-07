# -*- Coding:utf-8 -*-
"""

"""
from collections import OrderedDict


class UnionFind:

    def __init__(self, data=None, parent=None, sub=OrderedDict()):
        self._data = data
        self._parent = parent
        self._sub = sub

        pass

    def __getstate__(self):
        if len(self) == 0:
            # The state can't be an empty list.
            # We need to return a true value, or else __setstate__ won't be run.
            #
            # This could have been done more gracefully by always putting the state
            # in a tuple, but this way is backwards- and forwards- compatible with
            # previous versions of OrderedSet.
            return (None,)
        else:
            return list(self)

    def __setstate__(self, state):
        if state == (None,):
            self.__init__([])
        else:
            self.__init__(state)

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __str__(self):
        pass

    def _find(self):
        pass

    def same(self):
        pass

    def unite(self):
        pass
    
    def create_sub_union_find(self):
        pass
        

def union_find(*args, **kwargs):
    return UnionFind(*args, **kwargs)
