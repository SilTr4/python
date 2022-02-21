# 5) Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

import unittest


def count_of_numbers(numb_cnt: int, numb):  # не совсем уверен что это хороший код
    cnt = 0                                 # он же вроде все еще O(n)?
    for i in range(len(str(numb))):
        if str(numb)[i] == str(numb_cnt):
            cnt += 1
    return cnt


print(count_of_numbers(5, 505.453))


class TestCountOf_Numbers(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, count_of_numbers(5, 505.453))
        self.assertEqual(0, count_of_numbers(0, 1111111))
        self.assertEqual(6, count_of_numbers(9, 999.999))