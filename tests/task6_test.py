from unittest import TestCase, main
from tasks.task6 import wiggle_sort

class SixthTask(TestCase):
    def test_first(self):
        self.assertEqual(wiggle_sort([1,5,1,1,6,4]), [1,6,1,5,1,4])

    def test_second(self):
        self.assertEqual(wiggle_sort([1,3,2,2,3,1]), [2,3,1,3,1,2])


if __name__ =='__main__':
    main()