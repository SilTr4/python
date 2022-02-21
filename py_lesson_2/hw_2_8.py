# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

import unittest


def if_it_is_a_power_of_two(number):
    if number == 1:
        return True
    elif number % 2 != 0 or number == 0:
        return False
    return if_it_is_a_power_of_two(number / 2)


print(if_it_is_a_power_of_two(32))


class TestIfItIsAPowerOfTwo(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, if_it_is_a_power_of_two(64))
        self.assertEqual(False, if_it_is_a_power_of_two(0))
        self.assertEqual(False, if_it_is_a_power_of_two(100))
