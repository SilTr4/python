# 3. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import unittest


def min_index(arr: list):
    min = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min]:
            min = i
    return min, arr[min]


print(min_index([2, 3, 1, 4]))


class TestMinIndex(unittest.TestCase):
    def test_1(self):
        self.assertEqual((0, 1), min_index([1, 2, 3, 4, 5]))
        self.assertEqual((0, 1), min_index([1, 1, 1, 1]))
        self.assertEqual((1, -4), min_index([4, -4, 23, -2]))