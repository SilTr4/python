# Write a function that reverses a string. The input string is given as an array of characters s.


import unittest


def revers_a_string(arr: list):

    def helper(array, index):
        if index >= len(array) // 2:
            return
        array[len(array) - index - 1], array[index] = array[index], array[len(array) - index - 1]
        helper(array, index + 1)

    helper(arr, 0)
    return arr


print(revers_a_string(['f', 'g', 'a', 'f', 'B']))


class TestReversAString(unittest.TestCase):
    def test_1(self):
        self.assertEqual(['B', 'f', 'a', 'g', 'f'], revers_a_string(['f', 'g', 'a', 'f', 'B']))
        self.assertEqual(['d'], revers_a_string(['d']))
        self.assertEqual(['A', 'a', 'b', 'B'], revers_a_string(['B', 'b', 'a', 'A']))