from tasks.task7 import merge_in_place
from tasks.task10 import radix_sort
import random
import string
from unittest import TestCase, main


class FirstTask(TestCase):

    def generate_random_string(self, length, amount):
        letters = string.ascii_lowercase
        rand_string = [''.join(random.choice(letters) for i in range(length)) for i in range(amount)]
        return rand_string

    def checker(self, words):

        copy = [word for word in words]
        merge_in_place(words, 0, len(words)-1)

        self.assertEqual(radix_sort(copy), words)

    def test_first(self):
        words = self.generate_random_string(6, 10)
        self.checker(words)

    def test_second(self):
        words = self.generate_random_string(40, 7)
        self.checker(words)



if __name__ == '__main__':
    main()
