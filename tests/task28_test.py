from unittest import TestCase, main
from tasks.task28 import BloomFilter
from random import randint
from typing import List


class TwentyEighth(TestCase):
    @classmethod
    def ip_generator(self) -> str:
        return ".".join(str(randint(0, 255)) for _ in range(4))

    @classmethod
    def ip_array_maker(self, amount: int) -> List[str]:
        result = []
        for _ in range(amount):
            result.append(self.ip_generator())
        return result

    def checker(self, amount: int, prospect: float):
        instance = BloomFilter(amount, prospect)
        test_data = self.ip_array_maker(amount)

        for address in test_data:
            instance.add(address)

        for address in test_data:
            assert instance.look_up(address)

        errors_amount = 0
        _range = 10000

        for _ in range(_range):
            test_address = self.ip_generator()
            if test_address not in test_data:
                if instance.look_up(test_address):
                    errors_amount += 1

        if (errors_amount / _range) > prospect:
            print(f"Not enough accuracy: needed {prospect}, actual {errors_amount / _range}")
            assert False

    def test_first(self):
        self.checker(20, 0.002)

    def test_second(self):
        self.checker(10, 0.001)

    def test_third(self):
        self.checker(100, 0.01)


if __name__ == "__main__":
    main()
