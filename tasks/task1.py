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

# Оценка сложности работы алгоритма
# рассмотрим два числа длины n и m соответсвенно.
# в начале алгоритма мы должны выбрать первые m (m+1) цифр делимого так (result = result * 10 + i), чтобы число, составленное из них, превосходило делитель.
# после этого нам нужно найти максимальное число, которое при умножении на делитель будет давать наиболее близкое к выбранному нами "новому" делимому число.
# в наихудшем случае мы можем проделать до 10 проходов циклом while, пока не достигнем нужного множителя.
# т.е максимальное число операций на первом шаге равно 10*m.
# т.к нам нужно пройти по всем n цифрам делимого, то будем считать что наихудший случай (как при мервом шаге) повторяется n раз
# таким образом, мы n раз мы делаем 10*m операций => O(n*10*m)
