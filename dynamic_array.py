class DynamicArray(object):
    def __init__(self, val="", nxt=None):
        # val="" means empty node
        self.value = val
        self.next = nxt

    def __eq__(self, other):
        if other.value == '':
            return self.value == ''
        if self.value != other.value:
            return False
        return self.next == other.next

    def __str__(self, is_first=True):
        """
        In order to print out the symbol [ and ], the is_first
        variable is added to determine whether it is the first number
        """
        if self.value != '':
            return "[{}{}".format(self.value, self.next.__str__(False)) \
                if is_first \
                else ", {}{}".format(self.value, self.next.__str__(False))
        else:
            return '[]' if is_first else ']'

    def __iter__(self):
        return DynamicArrayIterator(self)


class DynamicArrayIterator(object):
    def __init__(self, pos):
        self.__pos = pos

    def __iter__(self):
        return self

    def __next__(self):
        # wzm
        if self.__pos.value == '':
            raise StopIteration()
        res = self.__pos.value
        self.__pos = self.__pos.next
        return res


def cons(v, lst):
    # llq
    return DynamicArray(v, lst)


def remove(lst, p):
    # llq
    if lst.value == '':
        raise Exception('The location accessed is not in the array!')
    if p == 0:
        return lst.next
    return cons(lst.value, remove(lst.next, p - 1))


def length(lst):
    # llq
    if lst.value == '':
        return 0
    else:
        return 1 + length(lst.next)


def member(v, lst):
    # llq
    if lst.value == '':
        return False
    if lst.value == v:
        return True
    return member(v, lst.next)


def reverse(lst, acc=DynamicArray()):
    # llq
    if lst.value == '':
        return acc
    return reverse(lst.next, DynamicArray(lst.value, acc))


def set(lst, p, v):
    # llq
    if lst.value == '' or p < 0:
        raise Exception('The location accessed is not in the array!')
    if p == 0:
        return cons(v, lst.next)
    return cons(lst.value, set(lst.next, p - 1, v))


def to_list(lst):
    # llq
    res = []
    for k in lst:
        res.append(k)
    return res


def from_list(v):
    # llq
    if len(v) == 0:
        return empty()
    return cons(v[0], from_list(v[1:]))


def find(lst, p):
    # wzm
    for k in lst:
        if p(k):
            return True
    return False


def filter(function, lst):
    # wzm
    res = DynamicArray()
    for v in lst:
        if function(v):
            res = cons(v, res)
    return reverse(res)


def map(function, *iters):
    # wzm
    res = DynamicArray()
    for args in zip(*iters):
        res = cons(function(*args), res)
    return reverse(res)


def reduce(function, lst, initializer=None):
    # wzm
    it = iterator(lst)
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


def iterator(lst):
    # llq
    return iter(lst)


def empty():
    # llq
    return DynamicArray()


def concat(lst1, lst2):
    # llq
    if lst2.value == '':
        return lst1
    return _concat_inner(reverse(lst1), lst2)


def _concat_inner(lst1, lst2):
    # llq
    if lst1.value == '':
        return lst2
    return _concat_inner(lst1.next, cons(lst1.value, lst2))
