from unittest import TestCase, main
from tasks.task7 import merge_in_place
import random


class FirstTask(TestCase):

    def merger(self, start, end):
        a = [random.randint(-100, 100) for __ in range(end+1)]
        merge_in_place(a, start, end)
        self.assertEqual(a, sorted(a))

    def test_first(self):
        self.merger(0, 10)

    def test_second(self):
        self.merger(0, 1001)



if __name__ == '__main__':
    main()
