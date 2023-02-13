def get_digits(num):
    digits = []
    while num:
        digits.append(num % 10)
        num //= 10
    return reversed(digits)


def division_algo(dividend, divider):
    result = 0
    remainder = 0
    i = 0
    for dig in get_digits(dividend):
        dig += remainder * 10
        while dig >= i * divider:
            i += 1
        if i:
            i -= 1
            remainder = dig - i * divider
        else:
            remainder = dig
        result = result * 10 + i

    return result, remainder


def checker(dividend, divider):
    result = division_algo(dividend, divider)
    answer = result[0] * divider + result[1]
    return answer == dividend


if __name__ == '__main__':
    print(checker(6565, 33))
