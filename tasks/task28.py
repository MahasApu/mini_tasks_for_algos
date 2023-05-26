import math
from random import randint
from bitset import BitSet


class Bloom_filter:
    def __init__(self, n):
        self.array = BitSet(n)
        self.universal_hash_funcs = {}

    def hash_f(self, k, n):
        i = 1
        while k > 0:
            c0, c1, c2, c3 = randint(1, n - 1), randint(1, n - 1), randint(1, n - 1), randint(1, n - 1)
            self.universal_hash_funcs[f"h{i}"] = [c0, c1, c2, c3]
            i += 1
            k -= 1

    def insert(self, id: str, n):
        parts_id = [int(x) for x in id.split('.')]
        for j in self.universal_hash_funcs.values():
            h = (j[0] * parts_id[0] + j[1] * parts_id[1] + j[2] * parts_id[2] + j[3] * parts_id[3]) % n
            self.array[h] = 1

    def lookup(self, id: str, n):
        parts_id = [int(x) for x in id.split('.')]
        flag = True
        for j in self.universal_hash_funcs.values():
            h = (j[0] * parts_id[0] + j[1] * parts_id[1] + j[2] * parts_id[2] + j[3] * parts_id[3]) % n
            if self.array[h] == 0:
                flag = False
        if flag:
            return "true"
        else:
            return "false"


if __name__ == "__main__":
    amount = 5
    probability = 0.99
    k = math.log(probability, 1 / 2)  # hash func amount
    b = k / math.log1p(2)  # bit per item
    print(k, b)
    n = int(amount * b)  # len of array in  Bloom_filter
    if n == 0:
        n = amount
    print(n)
    bloom_filter = Bloom_filter(n)
    bloom_filter.hash_f(k, n)
    bloom_filter.insert("193.24.134.56", n)
    bloom_filter.insert("194.54.74.96", n)
    bloom_filter.insert("23.25.134.86", n)
    bloom_filter.insert("52.26.124.56", n)
    bloom_filter.insert("193.27.134.56", n)
    print(bloom_filter.lookup("194.54.74.96", n))
    print(bloom_filter.lookup("193.27.134.56", n))
    print(bloom_filter.lookup("197.54.74.96", n))
    print(bloom_filter.lookup("177.54.74.96", n))
    print(bloom_filter.lookup("177.253.74.96", n))
