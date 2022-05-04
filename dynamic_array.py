class DynamicArray(object):
    def __init__(self, capacity=10, grow_factor=1.2):
        self.__grow_factor = grow_factor
        self.__length = 0
        self.__capacity = capacity  # Initialize chunk size to 10
        self.__start_num = -1
        self.__chunk = [None] * self.__capacity

    def add_element(self, element):
        if element is not None and type(element) != int:
            raise Exception('Input data must be int or None')
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
        assert type(other) == DynamicArray
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
    assert type(lst) == DynamicArray
    res = DynamicArray()
    for k in lst:
        res.add_element(k)
    res.add_element(v)
    return res


def remove(lst, p):
    # llq
    assert type(lst) == DynamicArray
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
    assert type(lst) == DynamicArray
    for k in lst:
        if v == k:
            return True
    return False


def reverse(lst):
    # llq
    assert type(lst) == DynamicArray
    tmp = []
    for k in lst:
        tmp.append(k)
    return from_list(tmp[::-1])


def set(lst, p, v):
    # llq
    assert type(lst) == DynamicArray
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
    assert type(lst) == DynamicArray
    res = []
    for k in lst:
        res.append(k)
    return res


def from_list(v):
    # llq
    assert type(v) == list
    res = DynamicArray()
    for k in v:
        res.add_element(k)
    return res


def find(lst, p):
    # wzm
    pass


def filter(lst, p):
    # wzm
    pass


def map(lst, p):
    # wzm
    pass


def reduce(lst, p):
    # wzm
    pass


def iterator(lst):
    # llq
    assert type(lst) == DynamicArray
    return iter(lst)


def empty():
    # llq
    return DynamicArray()


def concat(lst1, lst2):
    # llq
    assert type(lst1) == DynamicArray and type(lst2) == DynamicArray
    res = DynamicArray()
    for k in lst1:
        res.add_element(k)
    for k in lst2:
        res.add_element(k)
    return res
