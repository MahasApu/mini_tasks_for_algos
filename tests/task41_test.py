from random import randrange
from tasks.task41 import ImplicitTreap


def generator(start: int, end: int, test_data: list = None, size: int = None):
    if not test_data:
        test_data = [randrange(100) for _ in range(size)]
        implicit_treap = ImplicitTreap(array=test_data, rand=True)
        check_sum = sum(test_data[start:end + 1])
    else:
        implicit_treap = ImplicitTreap(array=test_data, rand=False)
        # implicit_treap.print_helper(implicit_treap.root, '', True)
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
