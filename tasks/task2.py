def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    length = max(len(str(x)), len(str(y)))
    if length % 2 == 1:
        length -= 1

    half_part = length // 2
    a = x // 10 ** half_part
    b = x % 10 ** half_part
    c = y // 10 ** half_part
    d = y % 10 ** half_part
    print(a,b,c,d,'.................', x, y)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return ac * 10 ** length + ad_plus_bc * 10 ** half_part + bd

print(karatsuba(1234212345621,3333333))