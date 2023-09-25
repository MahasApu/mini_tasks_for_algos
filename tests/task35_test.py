from tasks.task35 import Union_find_algo, griddy_algo


def checker(expr: list):
    answer1 = Union_find_algo(expr)[1]
    answer2 = griddy_algo(expr)[1]
    assert answer1 <= answer2


def test1():
    test_data = [['A', 3, 25], ['B', 4, 10], ['C', 1, 30], ['D', 3, 50], ['E', 3, 20]]
    checker(test_data)


def test2():
    test_data = [['A', 4, 25], ['B', 4, 35], ['C', 4, 30], ['D', 3, 50], ['E', 3, 20]]
    checker(test_data)


def test3():
    test_data = [['A', 3, 25], ['B', 4, 10], ['C', 1, 30], ['D', 3, 50], ['E', 3, 20]]
    checker(test_data)
