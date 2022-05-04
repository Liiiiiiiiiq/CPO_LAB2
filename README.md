# CPO_LW - lab 2 - variant 2

In lab 2, *Immutable Algorithms and Data Structure Implementation*, our
variant 2 aims to implement dynamic array using Python.

## Project structure

- `dynamic_array.py` -- implementation of `DynamicArray` class with `add`,
 `set`,`remove`,`filter`,`map` and other features.

- `dynamic_array_test.py` -- unit and PBT tests for `DynamicArray`.

## Features

- `add(elem)`: Add a new element to the end of array. If `capacity == length`,
 it will allocate a new chunk of memory by user-specified growing factor.
- `set(pos, elem)`: Set an element with specific index.
- `remove(pos)`: Remove an element by index.
- `size()`: Return the length of array.
- `member(elem)`: Return a boolean indicating whether the element is a member
 of the array.
- `reverse()`: reverse the array.
- `from_list(list)`: Conversion from built-in `list`.
- `to_list()`: Conversion to built-in `list`.
- `filter(pre)`: Filter data structure by specific predicate.
- `map(fun)`: Map elements of the array by specific function.
- `reduce(fun)`: Process elements of the array to build a return value by
 specific function.
- `\__iter\__` and `\__next\__`: Implementation of iterator in Python style.
- `\__add\__`: Operator `+` overloading, implement two arrays concatenate.

## Contribution

- Li Liquan (212320016@hdu.edu.cn)
  - GitHub repository created
  - Source code framework construction
  - implement features and tests: `add`, `set`, `remove`, `size`, `member`,
  `reverse`, `from_list`, `to_list`, `__add__`

- Wang Zimeng (1372178297@qq.com)
  - implement features and tests: `filter`, `map`, `reduce`, `__iter__`, `__next__`
  - write `README.md`

## Changelog

- 3.5.2022 14:46 -1
  - Build the project framework.

## Design notes

### Implementation restrictions

None

### unittest and PBT tests

- Unit testing is an essential practice in software development to detect
 defects in the software in the early development stage to save time and cost.
 It reduces or prevents production bugs, increases developer productivity,
 encourages modular programming. But it is time-consuming, can’t be challenging
 to cover all the code, and won’t catch all bugs.

- Property-based testing (PBT) is the approach to software testing that implies
 an automatic check of the function properties (predicates) specified by the tester.
 Checking, i.e. search for counter-examples is carried out using the automatically
 generated input data. PBT allows developers to increase the test coverage
 significantly and spend their time efficiently saving them the trouble of
 inventing the input data for tests on their own. But it does not cover all examples.