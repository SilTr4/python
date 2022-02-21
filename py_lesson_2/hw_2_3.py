# 3) Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
# ...Количество элементов (n) вводится с клавиатуры.

import unittest


def sum_of_numbs(numb: int):
    result = 0
    current_step = 1
    while numb != 0:
        result += current_step
        current_step /= 2 * (-1)
        numb -= 1
    return result


n = int(input('Введите число: '))
print(sum_of_numbs(n))


class TestSumOfNumbs(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0.666015625, sum_of_numbs(10))
        self.assertEqual(0, sum_of_numbs(0))
        self.assertEqual(0.5, sum_of_numbs(2))
