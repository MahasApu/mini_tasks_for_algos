from math import log, ceil, e
from bitarray import bitarray
from random import randint
from typing import Callable, List


class BloomFilter(object):
    '''
    Class for Bloom filter, using randomly generated hash function
    '''

    def __init__(self, items_amount: int, prospect: float):
        self.capacity = self.get_capacity(prospect, self.next_prime_num(items_amount))
        self.universal_hash = self.get_hash_funcs(ceil(log(prospect, 0.5)))
        self.bit_array = bitarray(self.capacity)
        self.bit_array.setall(0)

    def get_hash_funcs(self, hash_amount: int) -> List[Callable]:

        def hash_func(c0: int, c1: int, c2: int, c3: int) -> Callable:
            def get_hash(ip_address):
                ip_addr = [int(_) for _ in ip_address.split('.')]
                return ip_addr[0] * c0 + ip_addr[1] * c1 + ip_addr[2] * c2 + ip_addr[3] * c3

            return get_hash

        def funcs_generator(hash_amount: int) -> List[Callable]:
            hash_funcs = []
            for _ in range(hash_amount):
                c0, c1, c2, c3 = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
                hash_funcs.append(hash_func(c0, c1, c2, c3))
            return hash_funcs

        return funcs_generator(hash_amount)

    def add(self, item) -> None:
        for func in self.universal_hash:
            self.bit_array[func(item) % self.capacity] = 1

    def look_up(self, item) -> bool:
        for func in self.universal_hash:
            if not self.bit_array[func(item) % self.capacity]:
                return False
        return True

    @classmethod
    def next_prime_num(self, num: int) -> int:
        i = num
        while True:
            isPrime = True
            d = 2
            while d * d <= i:
                if i % d == 0:
                    isPrime = False
                    break
                d += 1
            if isPrime:
                return i
            i += 1

    def get_capacity(self, prospect: float, capacity: int) -> int:
        return ceil(ceil(log(prospect, 0.5)) / log(2, e)) * capacity
