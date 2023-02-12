from unittest import TestCase, main
from tasks.task1 import division_algo

class FirstTask(TestCase):
    def test_first(self):
        self.assertEqual(division_algo(4,4), (1,0))

    def test_second(self):
        self.assertEqual(division_algo(4,4), (1,0))


if __name__ =='__main__':
    main()