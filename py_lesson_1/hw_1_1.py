# 1) Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

import unittest

def sum_of_number(number: int):
    hundred = number // 100
    ten = (number % 100) // 10
    ones = number % 10
    print(hundred, ten, ones)
    return (hundred + ten + ones), (hundred * ten * ones)

print(sum_of_number(545))

class TestSumNumb(unittest.TestCase):
    def test_1(self):
        self.assertEqual((14, 100), sum_of_number(545))
        self.assertEqual((1, 0), sum_of_number(1))
        self.assertEqual((27, 729), sum_of_number(999))