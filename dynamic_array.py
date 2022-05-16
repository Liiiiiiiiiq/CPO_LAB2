from typing import Callable
from typing import Union
from typing import Any
from typing import Optional

DeType = Union[int, str, None]
Default = Union['DynamicArray', None]


class DynamicArrayIterator(object):
    def __init__(self, pos: Default) -> None:
        self.__pos = pos

    def __iter__(self) -> 'DynamicArrayIterator':
        return self

    def __next__(self) -> DeType:
        # wzm
        if self.__pos is None:
            raise TypeError()
        if self.__pos.value == '':
            raise StopIteration()
        res = self.__pos.value
        self.__pos = self.__pos.next
        return res


class DynamicArray(object):
    def __init__(self, val: DeType = "",
                 nxt: Optional['DynamicArray'] = None) -> None:
        # val="" means empty node
        self.value = val
        self.next = nxt

    def __eq__(self, other: 'object') -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        if other.value == '':
            return self.value == ''
        if self.value != other.value:
            return False
        return self.next == other.next

    def __str__(self, is_first: bool = True) -> str:
        """
        In order to print out the symbol [ and ], the is_first
        variable is added to determine whether it is the first number
        """
        if self.next is not None:
            return "[{}{}".format(self.value, self.next.__str__(False)) \
                if is_first \
                else ", {}{}".format(self.value, self.next.__str__(False))
        else:
            return '[]' if is_first else ']'

    def __iter__(self) -> 'DynamicArrayIterator':
        return DynamicArrayIterator(self)


def cons(v: DeType, lst: Optional['DynamicArray']) -> 'DynamicArray':
    # llq
    return DynamicArray(v, lst)


def remove(lst: Optional['DynamicArray'], p: int) -> Optional['DynamicArray']:
    # llq
    if lst is None:
        return None
    if lst.value == '':
        raise Exception('The location accessed is not in the array!')
    if p == 0:
        return lst.next
    return cons(lst.value, remove(lst.next, p - 1))


def length(lst: Optional['DynamicArray']) -> int:
    # llq
    if lst is None:
        return 0
    if lst.value == '':
        return 0
    else:
        return 1 + length(lst.next)


def member(v: DeType, lst: Optional['DynamicArray']) -> bool:
    # llq
    if lst is None:
        return False
    if lst.value == '':
        return False
    if lst.value == v:
        return True
    return member(v, lst.next)


def reverse(lst: Optional['DynamicArray'],
            acc: Optional['DynamicArray'] = DynamicArray()) \
        -> Optional['DynamicArray']:
    # llq
    if lst is None:
        return empty()
    if lst.value == '':
        return acc
    return reverse(lst.next, DynamicArray(lst.value, acc))


def set(lst: Optional['DynamicArray'], p: int, v: DeType) \
        -> Optional['DynamicArray']:
    # llq
    if lst is None or lst.value == '' or p < 0:
        raise Exception('The location accessed is not in the array!')
    if p == 0:
        return cons(v, lst.next)
    return cons(lst.value, set(lst.next, p - 1, v))


def to_list(lst: Optional['DynamicArray']) -> list[Any]:
    # llq
    if lst is None:
        return []
    res = []
    for k in lst:
        res.append(k)
    return res


def from_list(v: list[Any]) -> 'DynamicArray':
    # llq
    if len(v) == 0:
        return empty()
    return cons(v[0], from_list(v[1:]))


def find(lst: Optional['DynamicArray'], p: Callable[[Any], Any]) -> bool:
    # wzm
    if lst is None:
        return False
    for k in lst:
        if p(k):
            return True
    return False


def filter(function: Callable[[Any], Any],
           lst: Optional['DynamicArray']) -> Optional['DynamicArray']:
    # wzm
    if lst is None:
        return None
    res = DynamicArray()
    for v in lst:
        if function(v):
            res = cons(v, res)
    return reverse(res)


def map(function: Callable[..., Any], *iters: 'DynamicArray') \
        -> Optional['DynamicArray']:
    # wzm
    res = DynamicArray()
    for args in zip(*iters):
        res = cons(function(*args), res)
    return reverse(res)


def reduce(function: Callable[[Any, Any], Any],
           lst: Optional['DynamicArray'],
           initializer: Optional[int] = None) -> DeType:
    # wzm
    it = iterator(lst)
    if it is None:
        raise TypeError()
    if initializer is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError("reduce() of empty sequence with no "
                            "initial value") from None
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


def iterator(lst: Optional['DynamicArray']) -> 'DynamicArrayIterator':
    # llq
    if lst is None:
        raise StopIteration()
    return iter(lst)


def empty() -> 'DynamicArray':
    # llq
    return DynamicArray()


def concat(lst1: Optional['DynamicArray'],
           lst2: Optional['DynamicArray']) \
        -> Optional['DynamicArray']:
    # llq
    if lst1 is None or lst2 is None:
        raise TypeError()
    if lst2.value == '':
        return lst1
    return _concat_inner(reverse(lst1), lst2)


def _concat_inner(lst1: Optional['DynamicArray'],
                  lst2: Optional['DynamicArray']) \
        -> Optional['DynamicArray']:
    # llq
    if lst1 is None or lst2 is None:
        raise TypeError()
    if lst1.value == '':
        return lst2
    return _concat_inner(lst1.next, cons(lst1.value, lst2))
