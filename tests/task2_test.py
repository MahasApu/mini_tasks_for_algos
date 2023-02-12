from unittest import TestCase, main
from tasks.task2 import karatsuba


class SecondTest(TestCase):
    def test_first(self):
        self.assertEqual(karatsuba(1234, 5678), 7006652)

    def test_second(self):
        self.assertEqual(karatsuba(1234567, 5678), 7009871426)

    def test_third(self):
        self.assertEqual(karatsuba(87654321234567890987643345678987654345678998765432345678876543,
                                   8765656543321122145678987654321234567898765432123456),
                         768347674480161615126426316469686343602510190364584287466819333075714001220775312932789764639495906112192958492608)

    def test_fourth(self):
        self.assertEqual(karatsuba(9, 56788765678765766555432112345), 511098891108891898998889011105)

    def test_fifth(self):
        self.assertEqual(karatsuba(12345, 121),
                         1493745)

    def test_sixth(self):
        self.assertEqual(karatsuba(1234567654323456, 9878878987654322345678900987654321234567),
                         12196144459133674383095294318270592927384481025066103552)

    def test_seventh(self):
        self.assertEqual(karatsuba(12345, 5678), 70094910)


if __name__ == '__main__':
    main()
