# -*- Coding:utf-8 -*-
"""

"""
from nose.tools import eq_, assert_true, assert_false
from union_find import UnionFind, _isiterable
import pickle


def test_pickle():
    union_find1 = UnionFind('root')
    union_find1.data = union_find1.data + 'ooo'
    eq_(pickle.loads(pickle.dumps(union_find1)), union_find1)

    union_find1.create_sub_union_find('sub1')
    union_find1.create_sub_union_find('sub2')
    union_find1.parent = UnionFind('root2')
    eq_(pickle.loads(pickle.dumps(union_find1)), union_find1)


def test_empty_pickle():
    union_find1 = UnionFind()
    roundtrip = pickle.loads(pickle.dumps(union_find1))
    eq_(roundtrip, union_find1)


def test_same():
    union_find1 = UnionFind('root', subs=[])

    sub1 = union_find1.create_sub_union_find('sub1')
    union_find1.parent = UnionFind('root2', subs=[])
    sub2 = union_find1.create_sub_union_find('sub2')

    assert_true(sub1.same(sub2))
    assert_true(sub2.same(sub1))
    assert_true(sub1.same([sub1, sub2]))


def test_union():
    root1 = UnionFind('root')
    sub1 = root1.create_sub_union_find('sub1')

    roo2 = UnionFind('root2')
    sub2 = roo2.create_sub_union_find('sub2')

    sub2.unite(sub1)

    assert_true(sub1.same([sub1, sub2, root1, roo2]))


def test_copy():
    root1 = UnionFind('root')
    root1.create_sub_union_find('sub1')

    root1_copy = root1.copy()
    eq_(root1, root1_copy)
    assert_true(root1 is not root1_copy)


def test___str__():
    root1 = UnionFind('root')
    root1.create_sub_union_find('sub1')

    isinstance(root1.__str__(), str)


def test__isiterable():
    assert_false(_isiterable(12))