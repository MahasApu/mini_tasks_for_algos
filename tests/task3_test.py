from unittest import TestCase, main
from tasks.task3 import search

class ThirdTest(TestCase):
    def test_first(self):
        self.assertEqual(search([1,2,44,56,234,688],44), 2)

    def test_second(self):
        self.assertEqual(search([1,2,3,4,5,6,7,8,9,72,98,99,100,34567899876],546545), -1)

    def test_third(self):
        self.assertEqual(search([8,11,21,40,345,2777,5676,80000],80000),7)

    def test_fourth(self):
        self.assertEqual(search([7556,25532,88998,349992,12121212,600000000,77777777777], 7556), 0)

if __name__=='__main__':
    main()