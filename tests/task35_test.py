from tasks.task35 import Union_find_algo, greedy_algo


def checker(expr: list):
    answer1 = Union_find_algo(expr)[1]
    answer2 = greedy_algo(expr)[1]
    assert answer1 <= answer2


def test1():
    test_data = [['A', 3, 25], ['B', 4, 10], ['C', 1, 30], ['D', 3, 50], ['E', 3, 20]]
    checker(test_data)


def test2():
    test_data = [['A', 4, 25], ['B', 4, 35], ['C', 4, 30], ['D', 3, 50], ['E', 3, 20]]
    checker(test_data)


def test3():
    test_data = [['A', 1, 25], ['B', 1, 25], ['C', 1, 25], ['D', 1, 25], ['E', 3, 20]]
    checker(test_data)


def test4():
    test_data = [['A', 1, 25], ['B', 1, 10], ['C', 1, 30], ['D', 1, 50], ['E', 1, 20], ['F', 1, 60], ['G', 1, 70], ['H', 1, 50]]
    checker(test_data)

