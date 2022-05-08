class DynamicArray(object):
    def __init__(self, capacity=10, grow_factor=1.2):
        self.__grow_factor = grow_factor
        self.__length = 0
        self.__capacity = capacity  # Initialize chunk size to 10
        self.__start_num = -1
        self.__chunk = [None] * self.__capacity

    def add_element(self, element):
        if self.__length == self.__capacity:
            new_chunk_size = int(self.__capacity * self.__grow_factor) \
                             - self.__capacity
            self.__chunk += [None] * new_chunk_size
            self.__capacity = self.__capacity + new_chunk_size
        self.__chunk[self.__length] = element
        self.__length += 1

    def length(self):
        return self.__length

    def __eq__(self, other):
        if self.__length != other.length():
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    def __str__(self):
        return str(self.__chunk[:self.__length])

    def __iter__(self):
        return DynamicArrayIterator(self.__chunk, self.__length)


class DynamicArrayIterator(object):
    def __init__(self, lst, lng):
        self.__chunk = lst
        self.__length = lng
        self.__start_num = -1

    def __iter__(self):
        return self

    def __next__(self):
        # wzm
        self.__start_num += 1
        if self.__start_num >= self.__length:
            raise StopIteration()
        return self.__chunk[self.__start_num]


def cons(lst, v):
    # llq
    import copy
    res = copy.deepcopy(lst)
    res.add_element(v)
    return res


def remove(lst, p):
    # llq
    if p < 0 or p >= lst.length():
        raise Exception('The location accessed is not in the array!')
    res = DynamicArray()
    for idx, i in enumerate(lst):
        if idx != p:
            res.add_element(i)
    return res


def length(lst):
    # llq
    return lst.length()


def member(lst, v):
    # llq
    for k in lst:
        if v == k:
            return True
    return False


def reverse(lst):
    # llq
    tmp = []
    for k in lst:
        tmp.append(k)
    return from_list(tmp[::-1])


def set(lst, p, v):
    # llq
    if v is not None and type(v) != int:
        raise Exception('Input data must be int or None')
    if p < 0 or p >= lst.length():
        raise Exception('The location accessed is not in the array!')
    res = DynamicArray()
    for idx, i in enumerate(lst):
        if p == idx:
            res.add_element(v)
        else:
            res.add_element(i)
    return res


def to_list(lst):
    # llq
    res = []
    for k in lst:
        res.append(k)
    return res


def from_list(v):
    # llq
    res = DynamicArray()
    for k in v:
        res.add_element(k)
    return res


def find(lst, p):
    # wzm
    for k in lst:
        if p(k):
            return True
    return False


def filter(function, lst):
    # wzm
    res = DynamicArray()
    for k in lst:
        if function(k):
            res.add_element(k)
    return res


def map(function, *iters):
    # wzm
    res = DynamicArray()
    for args in zip(*iters):
        res.add_element(function(*args))
    return res


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
    res = DynamicArray()
    for k in lst1:
        res.add_element(k)
    for k in lst2:
        res.add_element(k)
    return res
