import math 
from random import randint 
from bitset import BitSet 
 
 
class Bloom_filter: 
    def __init__(self, amount: int, probability: int): 
 
       
        self.amount = amount 
        self.probability = probability 
        self.k = math.log(self.probability, 1 / 2)  # hash func amount 
        self.b = self.k / math.log1p(2)  # bit per item 
        self.n = int(self.amount * self.b)  # len of array in  Bloom_filter 
         
        if self.n == 0: 
            self.n = amount 
        self.universal_hash_funcs = {} 
        self.hash_f(self.k, self.n) 
        self.array = BitSet(self.n) 
         
 
    def hash_f(self, k, n): 
        i = 1 
        while k > 0: 
            c0, c1, c2, c3 = randint(1, n - 1), randint(1, n - 1), randint(1, n - 1), randint(1, n - 1) 
            self.universal_hash_funcs[f"h{i}"] = [c0, c1, c2, c3] 
            i += 1 
            k -= 1 
 
    def insert(self, id: str, n): 
        parts_id = [int(x) for x in id.split('.')] 
        for coef_array in self.universal_hash_funcs.values(): 
            h = (coef_array[0] * parts_id[0] + coef_array[1] * parts_id[1] + coef_array[2] * parts_id[2] + coef_array[3] * parts_id[3]) % n 
            self.array[h] = 1 
 
    def lookup(self, id: str, n): 
        parts_id = [int(x) for x in id.split('.')] 
        flag = True 
        for coef_array in self.universal_hash_funcs.values(): 
            h = (coef_array[0] * parts_id[0] + coef_array[1] * parts_id[1] + coef_array[2] * parts_id[2] + coef_array[3] * parts_id[3]) % n 
            if self.array[h] == 0: 
                flag = False 
        if flag: 
            return True 
        else: 
            return False 
 
 
if name == "__main__": 
    n = 5 
    bloom_filter = Bloom_filter(n, 0.99) 
    n = bloom_filter.n  
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