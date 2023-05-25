from math import log, ceil, e
from bitarray import bitarray
from random import randint
from typing import Callable, List


class BloomFilter(object):
    '''
    Class for Bloom filter, using randomly generated hash function
    '''

    def __init__(self, items_amount: int, prospect: float):
        self.capacity = ceil(items_amount * log(e, 0.5) * log(prospect, 2))
        self.k = ceil(log(2) * self.capacity / items_amount)
        self.universal_hash = self.get_hash_funcs(self.capacity, self.k)
        self.bit_array = bitarray(self.capacity)
        self.bit_array.setall(0)

    def get_hash_funcs(self, capacity: int, hash_amount: int) -> List[Callable]:
        #
        def hash_func(rand_num: int, capacity):
            def get_hash(num):
                return (num * rand_num) % capacity

            return get_hash

        def hash_generator(capacity, hash_amount):
            funcs = []
            for _ in range(hash_amount):
                funcs.append(hash_func(randint(1, 10000), capacity))
            return funcs

        return hash_generator(capacity, hash_amount)

    def get_ip_hash(self, ip_address):

        ip_addr = [int(_) for _ in ip_address.split('.')]
        for i in range(len(ip_addr)):
            if ip_addr[i] == 0:
                ip_addr[i] = 1

        return ip_addr[0] * ip_addr[1] * ip_addr[2] * ip_addr[3]

    def insert(self, item) -> None:
        ip_adr = self.get_ip_hash(item)
        for func in self.universal_hash:
            index = func(ip_adr)
            self.bit_array[index] = 1

    def look_up(self, item) -> bool:
        ip_adr = self.get_ip_hash(item)
        for func in self.universal_hash:
            index = func(ip_adr)
            if not self.bit_array[index]:
                return False
        return True

    @classmethod
    def next_prime_num(self, num: int) -> int:
        i = num + 1
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
