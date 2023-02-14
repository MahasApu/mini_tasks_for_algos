from unittest import TestCase, main
from tasks.task5 import checker


class SecondTest(TestCase):
    def test_first(self):
        self.assertEqual(checker([3, 0, 6, 1, 5]), 3)

    def test_second(self):
        self.assertEqual(checker([1, 3, 1]), 1)

    def test_third(self):
        self.assertEqual(checker([0]), 0)

    def test_fourth(self):
        self.assertEqual(checker([11, 20, 33]), 3)

    def test_fifth(self):
        self.assertEqual(checker([8]), 1)


if __name__ == '__main__':
    main()
