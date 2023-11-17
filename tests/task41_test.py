from random import randrange
from tasks.task41 import ImplicitTreap


def generator(start: int, end: int, test_data: list = None, size: int = None):
    implicit_treap = ImplicitTreap()
    if not test_data:
        test_data = [randrange(size ** size) for _ in range(size)]
        for index, value in enumerate(test_data):
            implicit_treap.insert(index, value)
        check_sum = sum(test_data[start:end + 1])
    else:
        for index, item in enumerate(test_data):
            value, priority = item
            implicit_treap.insert(index, value, priority)
        tmp = [node[0] for node in test_data]
        check_sum = sum(tmp[start:end + 1])

    assert implicit_treap.sum(start, end) == check_sum


def test1():
    test_data = [(5, 6), (24, 8), (42, 9), (13, 4), (99, 11), (2, 7), (17, 10)]
    generator(5, 6, test_data=test_data)


def test2():
    generator(5, 7, size=7)


def test3():
    generator(0, 7, size=7)
