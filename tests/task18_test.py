from unittest import TestCase, main
from tasks.task18 import to_calc


class EighteenTask(TestCase):
    def checker(self, expr: str, for_check: str):
        self.assertEqual(to_calc(expr.split()), eval(for_check))

    def test_first(self):
        self.checker('4 + 8 + 1 ^ 32', '4 + 8 + 1 ** 32')

    def test_second(self):
        self.checker('( 11 / 11 ) * 12 - ( 1 + 3 ) ^ 2', '( 11 //11 ) * 12 - (1 + 3) ** 2')

    def test_third(self):
        self.checker('( 1 + ( ( ( ( 33 & 11 ) * 2 ) ) - 1 ) )', '( 1 + ( ( ( (33 & 11) * 2 ) ) - 1 ) )')

    def test_fourth(self):
        self.checker('4 ^ 3 ^ 2', '4**3**2')
    # Sample
    # def test_number(self):
    #     self.checker(expr)

if __name__ == '__main__':
    main()
