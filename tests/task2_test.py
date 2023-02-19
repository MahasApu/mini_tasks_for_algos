from unittest import TestCase, main
from tasks.task2 import karatsuba


class SecondTest(TestCase):
    def mult(self, num1, num2):
        self.assertEqual(karatsuba(num1,num2), (num1*num2))
    def test_first(self):
        self.mult( 1234, 5678)

    def test_second(self):
        self.mult (1234567, 5678)

    def test_third(self):
        self.mult(87654321234567890987643345678987654345678998765432345678876543,
                                   8765656543321122145678987654321234567898765432123456)


    def test_fourth(self):
        self.mult(9, 56788765678765766555432112345)

    def test_fifth(self):
        self.mult(12345, 121)

    def test_sixth(self):
        self.mult(1234567654323456, 9878878987654322345678900987654321234567)

    def test_seventh(self):
        self.mult(12345, 5678)


if __name__ == '__main__':
    main()
