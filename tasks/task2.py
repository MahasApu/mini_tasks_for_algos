def getlen(num):
    l = 1
    while num // 10:
        num //= 10
        l += 1
    return l


def karatsuba(x, y):
    if x // 10 == 0 or y // 10 == 0:
        return x * y

    length = max(getlen(x), getlen(y))
    if length % 2 == 1:
        length -= 1

    half_part = length // 2
    a = x // 10 ** half_part
    b = x % 10 ** half_part
    c = y // 10 ** half_part
    d = y % 10 ** half_part

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * 10 ** length + ad_plus_bc * 10 ** half_part + bd
