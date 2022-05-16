import unittest
from hypothesis import given

import hypothesis.strategies as st

from dynamic_array import DynamicArray
from dynamic_array import cons, remove, length, member
from dynamic_array import reverse, set, to_list, from_list
from dynamic_array import find, filter, map, reduce
from dynamic_array import iterator, empty, concat
from typing import Any


class TestDynamicArray(unittest.TestCase):

    def test_api(self) -> None:
        empty_ = DynamicArray()
        l1 = cons(None, cons(1, empty_))
        l2 = cons(1, cons(None, empty_))
        self.assertEqual(str(empty_), "[]")
        self.assertEqual(str(l1), "[None, 1]")
        self.assertEqual(str(l2), "[1, None]")
        self.assertNotEqual(empty_, l1)
        self.assertNotEqual(empty_, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(None, cons(1, empty_)))
        self.assertEqual(length(empty_), 0)
        self.assertEqual(length(l1), 2)
        self.assertEqual(length(l2), 2)
        self.assertEqual(str(remove(l1, 0)), "[1]")
        self.assertEqual(str(remove(l1, 1)), "[None]")
        self.assertFalse(member(None, empty_))
        self.assertTrue(member(None, l1))
        self.assertTrue(member(1, l1))
        self.assertFalse(member(2, l1))
        self.assertEqual(l1, reverse(l2))
        self.assertEqual(to_list(l1), [None, 1])
        self.assertEqual(l1, from_list([None, 1]))
        self.assertEqual(concat(l1, l2), from_list([None, 1, 1, None]))
        buf = []
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [None, 1])
        lst = to_list(l1) + to_list(l2)
        for e in l1:
            lst.remove(e)
        for e in l2:
            lst.remove(e)
        self.assertEqual(lst, [])

    def test_set(self) -> None:
        # llq
        empty_ = DynamicArray()

        l1 = cons(1, cons(None, empty_))
        l2 = cons(2, cons(1, empty_))

        self.assertEqual(str(set(l1, 0, None)), '[None, None]')
        self.assertEqual(str(set(l2, 1, 2)), '[2, 2]')

    @given(st.lists(st.integers()))
    def test_size(self, a: list[Any]) -> None:
        # llq
        b = from_list(a)
        self.assertEqual(length(b), len(a))

    def test_reverse(self) -> None:
        # llq
        a = [1, 3, 4, None, 4]
        b = from_list(a)
        self.assertEqual(str(reverse(b)), '[4, None, 4, 3, 1]')

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a: list[Any]) -> None:
        # llq
        self.assertEqual(to_list(from_list(a)), a)

    def test_find(self) -> None:
        # wzm
        a = [1, 3, 4, None, 4]
        arr = from_list(a)
        self.assertTrue(find(arr, lambda x: x is None))
        self.assertTrue(find(arr, lambda x: x % 2 == 0))
        self.assertTrue(find(arr, lambda x: x % 2 != 0))
        self.assertFalse(find(arr, lambda x: x == 2))

    @given(st.lists(st.integers()))
    def test_filter(self, a: list[Any]) -> None:
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
    def test_map(self, a: list[int], b: list[int], c: list[int]) -> None:
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
        self.assertEqual(to_list(map(lambda x, y, z: x + y - z, arr,
                                     arr1, arr2)), result)
        d = [1, 2, 3]
        arr_0 = from_list(d)
        e = [1, None, 9]
        arr_1 = from_list(e)
        with self.assertRaises(TypeError):
            map(lambda x, y: x + y, arr_0, arr_1)

    @given(st.lists(st.integers()), st.integers())
    def test_reduce(self, a: list[int], b: int) -> None:
        # wzm
        arr = from_list(a)
        if length(arr) == 0:
            self.assertEqual(b, reduce(lambda x, y: x + y, arr, b))
            with self.assertRaises(TypeError):
                reduce(lambda x, y: x + y, arr)
        else:
            from functools import reduce as gt_reduce
            result = gt_reduce(lambda x, y: x + y, a)
            self.assertEqual(reduce(lambda x, y: x + y, arr), result)
            result = gt_reduce(lambda x, y: x + y, a, b)
            self.assertEqual(reduce(lambda x, y: x + y, arr, b), result)

    def test_iter(self) -> None:
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

    def test_empty(self) -> None:
        # llq
        a = empty()
        b = from_list([])
        self.assertEqual(a, b)

    @given(st.lists(st.integers()),
           st.lists(st.integers()),
           st.lists(st.integers()))
    def test_monoid(self, a: list[int], b: list[int], c: list[int]) -> None:
        # llq
        da = from_list(a)
        db = from_list(b)
        dc = from_list(c)
        self.assertEqual(concat(concat(da, db), dc),
                         concat(da, concat(db, dc)))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst: list[int]) -> None:
        # llq
        a = from_list(lst)
        self.assertEqual(concat(empty(), a), a)
        self.assertEqual(concat(a, empty()), a)

    def test_immutability(self) -> None:
        a = from_list([1, 2, 3, 4, 5, 6, 7, 8, 3, 2])
        # do some operations on a
        cons(22, a)
        remove(a, 8)
        set(a, 0, 88)
        reverse(a)
        self.assertEqual(str(a), '[1, 2, 3, 4, 5, 6, 7, 8, 3, 2]')

