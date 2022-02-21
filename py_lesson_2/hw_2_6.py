# 6) Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

import unittest


def the_biggest_numb(arr: list):
    current_numb = 0
    the_highest_sum = 0
    for i in range(len(arr)):
        if type(arr[i]) == int and arr[i] >= 0:
            numb = arr[i]
            sums = 0
            while numb != 0:
                sums += numb % 10
                numb //= 10
            if sums > the_highest_sum:
                current_numb = arr[i]
                the_highest_sum = sums
    return current_numb, the_highest_sum


print(the_biggest_numb([1111, -123, 'вфвфв', 999]))


class TestTheBiggestNumb(unittest.TestCase):
    def test_1(self):
        self.assertEqual((999, 27), the_biggest_numb([1111, -123, 'вфвфв', 999]))
        self.assertEqual((0, 0), the_biggest_numb(['fafaf', 'agdbf', -222, -111]))