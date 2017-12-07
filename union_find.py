# -*- Coding:utf-8 -*-
"""

"""
from copy import copy


def _isiterable(obj, but_str_bytes=True):
    """
    :param obj:
    :param but_str_bytes: most of time, we don't need str and bytes
    :return:
    """
    from collections import Iterable
    if but_str_bytes and isinstance(obj, (str, bytes, bytearray)):
        return False
    else:
        return isinstance(obj, Iterable)


class UnionFind(object):
    """
    This design don't consider the balance of union find tree (because it's difficult to maintain the rank),
    may be need to be improved in the future!
    """

    def __init__(self, data=None, parent=None, subs=list()):
        self._data = data
        self._parent = parent
        self._subs = subs

    def __getstate__(self):
        return self._data, self._parent, self._subs

    def __setstate__(self, state):
        self.__init__(*state)

    def __eq__(self, other):
        if self is other:
            return True

        if other is None:
            return False

        # We can ensure that the max rank of union-find <= 2
        if self._parent is None and other.parent is None:
            if self._data != other.data:
                return False
            if len(self._subs) != len(other.subs):
                return False
            for self_subs, other_subs in zip(self._subs, other.subs):
                if self_subs.data != other_subs.data:
                    return False
            return True
        elif self._parent is not None and other.parent is not None:
            return self._parent == other.parent
        else:
            return False

    def __str__(self):
        return ("parent: {0}\n"
                "data:   {1}\n"
                "subs:    {2}\n".format(self._parent, self._data, self._subs))

    def get_data(self):
        return copy(self._data)
    
    def set_data(self, data):
        self._data = data
    
    data = property(get_data, set_data)

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        """the unique parent entry to ensure that no-indirect-parent"""
        self._parent = parent

        if self._parent is not None:
            self._compress_path()

    def _compress_path(self):
        for item in self._subs:
            item.parent = self._parent
        self._subs = list()

    parent = property(get_parent, set_parent)

    def get_subs(self):
        return self._subs

    subs = property(get_subs)

    def same(self, other_union_finds):
        if not _isiterable(other_union_finds):
            other_union_finds = [other_union_finds]

        for each_other_union_find in other_union_finds:
            if each_other_union_find is None:
                return False

            if self._parent is None:
                if self == each_other_union_find.parent:
                    return True
                else:
                    return False
            else:
                return self._parent.same(each_other_union_find)

    def unite(self, other_union_finds):
        if not _isiterable(other_union_finds):
            other_union_finds = [other_union_finds]

        for each_other_union_find in other_union_finds:
            self._unite(each_other_union_find)
    
    def _unite(self, other_union_find):
        if self.same(other_union_find):
            return

        other_union_find.parent = self
        if self.parent is None:
            self._subs.append(other_union_find)
    
    def create_sub_union_find(self, data=None):
        subs = UnionFind(data)
        if self._parent is None:
            subs.parent = self
        else:
            subs.parent = self._parent

        if self.parent is None:
            self._subs.append(subs)

        return subs

    def copy(self):
        """shallow copy"""
        
        return UnionFind(self.data, self.parent, self.subs)

