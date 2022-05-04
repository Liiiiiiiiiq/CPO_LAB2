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

    def get_chunk(self):
        # Used to read elements in a dynamic array
        return [self.__chunk[i] for i in range(self.__length)]

    def length(self):
        return self.__length

    def __eq__(self, other):
        assert type(other) == DynamicArray
        if self.__length != other.length():
            return False
        t = other.get_chunk()
        for i in range(self.__length):
            if self.__chunk[i] != t[i]:
                return False
        return True

    def __str__(self):
        return str(self.__chunk[:self.__length])

    def __iter__(self):
        a = DynamicArray()
        for i in range(self.__length):
            a.add_element(self.__chunk[i])
        return a

    def __next__(self):
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
    chunk = lst.get_chunk()
    for i in range(lst.length()):
        if i != p:
            res.add_element(chunk[i])
    return res


def length(lst):
    # llq
    return lst.length()


def member(lst, v):
    # llq
    assert type(lst) == DynamicArray
    chunk = lst.get_chunk()
    return v in chunk


def reverse(lst):
    # llq
    assert type(lst) == DynamicArray
    res = DynamicArray()
    chunk = lst.get_chunk()[::-1]
    for k in chunk:
        res.add_element(k)
    return res


def set(lst, p, v):
    # llq
    assert type(lst) == DynamicArray
    if v is not None and type(v) != int:
        raise Exception('Input data must be int or None')
    if p < 0 or p >= lst.length():
        raise Exception('The location accessed is not in the array!')
    res = DynamicArray()
    chunk = lst.get_chunk()
    for i in range(lst.length()):
        if p == i:
            res.add_element(v)
        else:
            res.add_element(chunk[i])
    return res


def to_list(lst):
    # llq
    assert type(lst) == DynamicArray
    return lst.get_chunk()


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
    pos = 0
    chunk = lst.get_chunk()

    def get_next():
        nonlocal pos
        if pos == lst.length():
            raise StopIteration
        tmp = chunk[pos]
        pos += 1
        return tmp

    return get_next


def empty():
    # llq
    return DynamicArray()


def concat(lst1, lst2):
    # llq
    assert type(lst1) == DynamicArray and type(lst2) == DynamicArray
    res = DynamicArray()
    for k in lst1.get_chunk():
        res.add_element(k)
    for k in lst2.get_chunk():
        res.add_element(k)
    return res
