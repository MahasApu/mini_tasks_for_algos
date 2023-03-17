def counting_sort(words, pos):
    ascii_len = 128
    buffer = [0 for __ in range(ascii_len)]
    amount = len(words)
    result = ['' for __ in range(amount)]

    for word in words:
        buffer[ord(word[pos])] += 1

    for i in range(ascii_len - 1, -1, -1):
        amount -= buffer[i]
        buffer[i] = amount

    for word in words:
        result[buffer[ord(word[pos])]] = word
        buffer[ord(word[pos])] += 1

    return result


def radix_sort(words):
    len_word = len(words[0])
    for pos in range(len_word - 1, -1, -1):
        words = counting_sort(words, pos)
    return words
