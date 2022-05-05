# CPO_LW - lab 2 - variant 2

In lab 2, *Immutable Algorithms and Data Structure Implementation*, our
variant 2 aims to implement dynamic array using Python.

## Project structure

- `dynamic_array.py` -- includes class `DynamicArray` with methods `__eq__` and `__str__`,
 class `DynamicArrayIterator` with `__iter__` and `__next__`,
 and functions `cons`, `remove`, `length`, `member`, `reverse`, `set`,
 `to_list`, `from_list`,
 `find`, `filter`, `map`, `reduce`, `iterator`, `empty`, and `concat`.

- `dynamic_array_test.py` -- unit and PBT tests for classes and functions in `dynamic_array.py`.

## Features

- `cons(lst, v)`: copy array `lst` as a new one and add
 a new element `v` to the end of the new.
 If `capacity == length`,it will allocate a new chunk of memory
 by user-specified growing factor.
- `remove(lst, pos)`: keep `lst` constant, return a new array
 that remove element at `pos`.
- `length(lst)`: return the length of `lst`.
- `member(lst, v)`: return a boolean indicating whether
 the element `v` is a member of `lst`.
- `reverse(lst)`:  keep `lst` constant, return a reverse array of `lst`.
- `set(lst, pos, v)`: copy array `lst` as a new one and
 set a new element `v` at `pos`.
- `to_list(lst)`: convert `lst` to built-in `list`.
- `from_list(list)`: convert from built-in `list`.
- `find(lst, pred)`: find element by specific predicate, return a boolean value.
- `filter(pred, lst)`: keep `lst` constant, filter data structure by specific predicate.
- `map(func, *iters)`: map elements of arrays by specific function,
 return a new array and keep `*iters` constant.
- `reduce(func, lst, initializer=None)`: process elements of the array `lst` to
 build a return value by
 specific function.
- `iterator(lst)`: return an iterator of `lst`.
- `empty()`: return an empty instance of `DynamicArray`.
- `concat(lst1, lst2)`: keep `lst1` and `lst2` constant,
 return a new array of two arrays concatenate.

## Contribution

- Li Liquan (212320016@hdu.edu.cn)
  - GitHub repository created
  - implement classes `DynamicArray`, `DynamicArrayIterator`
  - implement features and tests: `cons`, `remove`, `length`, `member`,
  `reverse`, `set`, `to_list`, `from_list`, `iterator`, `empty`, `concat`

- Wang Zimeng (1372178297@qq.com)
  - implement features and tests: `find`, `filter`, `map`, `reduce`
  - write `README.md`

## Changelog

- 3.5.2022 19:00 -5
  - Wang Zimeng update `README.md`.
- 3.5.2022 17:44 -4
  - Wang Zimeng commits codes.
- 3.5.2022 12:22 -3
  - Li Liquan commits codes.
- 3.5.2022 11:21 -2
  - Initial commit.
- 3.5.2022 14:46 -1
  - Build the project framework.

## Design notes

### Implementation restrictions

None

### Compare mutable and immutable implementation

- Mutable data refers to a database structure in which data can be changed.
 Any data changes made simply overwrite and replace the previous record.
 This means that previous iterations of data are lost unless there is
 a system of back-ups and transaction logs that track changes.

- Immutable data cannot be changed, meaning that the values inside
 them can't be added, removed, moved or swapped. Instead of changing
 the data structure you make a new version of the data structure
 which is a separate value. Such data structure more relevant for
 multi-thread programming.