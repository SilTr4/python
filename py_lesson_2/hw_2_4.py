# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


import unittest


def is_it_true(numb: int) -> bool:
    current_sum = 0
    result = False
    cnter = numb
    while cnter != 0:
        current_sum += cnter
        cnter -= 1
    if current_sum == (numb * (numb + 1) / 2):
        result = True
    return result


print(is_it_true(5))


class TestIsItTrue(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, is_it_true(5))
        self.assertEqual(True, is_it_true(0))
        self.assertEqual(True, is_it_true(999))
