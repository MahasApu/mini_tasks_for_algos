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

    def test_first(self):
        a = BloomFilter(1000, 0.01)
        a.insert("0.73.0.1")
        assert False == a.look_up("0.73.0.2")

    def test_second(self):
        a = BloomFilter(1000, 0.01)
        a.insert("848.233.22.123")
        a.insert("192.221.0.2")
        a.insert("292.168.0.0")
        assert [True, True, True] == [a.look_up("848.233.22.123"), a.look_up("192.221.0.2"), a.look_up("292.168.0.0")]

    def test_third(self):
        a = BloomFilter(1000, 0.01)
        ip_adr = self.ip_generator()
        a.insert(ip_adr)
        assert True == a.look_up(ip_adr)



if __name__ == "__main__":
    main()
