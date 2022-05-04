import unittest
from hypothesis import given

import hypothesis.strategies as st

from dynamic_array import *


class TestDynamicArray(unittest.TestCase):

    def test_api(self):
        empty_ = DynamicArray()

        l1 = cons(cons(empty_, 1), None)
        l2 = cons(cons(empty_, None), 1)
        self.assertEqual(str(empty_), "[]")
        self.assertEqual(str(l1), "[1, None]")
        self.assertEqual(str(l2), "[None, 1]")
        self.assertNotEqual(empty_, l1)
        self.assertNotEqual(empty_, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(cons(empty_, 1), None))
        self.assertEqual(length(empty_), 0)
        self.assertEqual(length(l1), 2)

        self.assertEqual(length(l2), 2)
        self.assertEqual(str(remove(l1, 0)), "[None]")
        self.assertEqual(str(remove(l1, 1)), "[1]")
        self.assertFalse(member(empty_, None))
        self.assertTrue(member(l1, None))
        self.assertTrue(member(l1, 1))
        self.assertFalse(member(l1, 2))
        self.assertEqual(l1, reverse(l2))
        self.assertEqual(to_list(l1), [1, None])
        self.assertEqual(l1, from_list([1, None]))
        self.assertEqual(concat(l1, l2), from_list([1, None, None, 1]))
        buf = []
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [1, None])
        lst = to_list(l1) + to_list(l2)
        for e in l1:
            lst.remove(e)
        for e in l2:
            lst.remove(e)
        self.assertEqual(lst, [])

    def test_set(self):
        # llq
        empty_ = DynamicArray()

        l1 = cons(cons(empty_, 1), None)
        l2 = cons(cons(empty_, 2), 1)

        self.assertEqual(str(set(l1, 0, None)), '[None, None]')
        self.assertEqual(str(set(l2, 1, 2)), '[2, 2]')

    @given(st.lists(st.integers()))
    def test_size(self, a):
        # llq
        b = from_list(a)
        self.assertEqual(length(b), len(a))

    def test_reverse(self):
        # llq
        a = [1, 3, 4, None, 4]
        b = from_list(a)
        self.assertEqual(str(reverse(b)), '[4, None, 4, 3, 1]')

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        # llq
        self.assertEqual(to_list(from_list(a)), a)

    def test_find(self):
        # wzm
        a = [1, 3, 4, None, 4]
        b = from_list(a)
        self.assertEqual(find(a, lambda x: x is None), True)
        self.assertEqual(find(a, lambda x: x % 2 == 0), True)
        self.assertEqual(find(a, lambda x: x % 2 != 0), True)
        self.assertEqual(find(a, lambda x: x == 2), False)

    @given(st.lists(st.integers()))
    def test_filter(self, a):
        # wzm
        from builtins import filter as gt_filter
        arr = from_list(a)
        result = list(gt_filter(lambda x: x % 2 == 0, a))
        self.assertEqual(to_list(filter(lambda x: x % 2 == 0, arr)), result)
        result = list(gt_filter(lambda x: x % 2 != 0, a))
        self.assertEqual(to_list(filter(lambda x: x % 2 != 0, arr)), result)

    @given(st.lists(st.integers()),
           st.lists(st.integers()),
           st.lists(st.integers()))
    def test_map(self, a, b, c):
        # wzm
        from builtins import map as gt_map
        arr = from_list(a)
        result = list(gt_map(lambda x: x ** 2, a))
        self.assertEqual(to_list(map(lambda x: x ** 2, arr)), result)
        result = list(gt_map(lambda x, y: x + y, a, b))
        arr1 = from_list(b)
        self.assertEqual(to_list(map(lambda x, y: x + y, arr, arr1)), result)
        arr2 = from_list(c)
        result = list(gt_map(lambda x, y, z: x + y - z, a, b, c))
        self.assertEqual(to_list(map(lambda x, y, z: x + y - z, arr, arr1, arr2)), result)
        a = [1, 2, 3]
        arr_0 = from_list(a)
        c = [1, None, 9]
        arr_1 = from_list(c)
        with self.assertRaises(TypeError):
            map(lambda x, y: x + y, arr_0, arr_1)

    @given(st.lists(st.integers()), st.integers())
    def test_reduce(self, a, b):
        # wzm
        arr = from_list(a)
        if arr.length() == 0:
            self.assertEqual(b,reduce(lambda x, y: x + y, arr, b))
            with self.assertRaises(TypeError):
                reduce(lambda x, y: x + y, arr)
        else:
            from functools import reduce as gt_reduce
            result = gt_reduce(lambda x, y: x + y, a)
            self.assertEqual(reduce(lambda x, y: x + y, arr), result)
            result = gt_reduce(lambda x, y: x + y, a, b)
            self.assertEqual(reduce(lambda x, y: x + y, arr, b), result)

    def test_iter(self):
        # llq
        x = [1, 2, 3]
        lst = from_list(x)
        tmp = []
        try:
            it = iterator(lst)
            while True:
                tmp.append(next(it))
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst), tmp)
        it = iterator(empty())
        self.assertRaises(StopIteration, lambda: next(it))

    def test_empty(self):
        # llq
        a = empty()
        b = from_list([])
        self.assertEqual(a, b)

    @given(st.lists(st.integers()),
           st.lists(st.integers()),
           st.lists(st.integers()))
    def test_monoid(self, a, b, c):
        # llq
        da = from_list(a)
        db = from_list(b)
        dc = from_list(c)
        self.assertEqual(concat(concat(da, db), dc),
                         concat(da, concat(db, dc)))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        # llq
        a = from_list(lst)
        self.assertEqual(concat(empty(), a), a)
        self.assertEqual(concat(a, empty()), a)
