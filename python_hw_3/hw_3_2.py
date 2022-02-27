# 2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import unittest


def change_min_max(arr: list):
    min = 0
    max = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max]:
            max = i
        elif arr[i] < arr[min]:
            min = i
    arr[min], arr[max] = arr[max], arr[min]
    return arr


print(change_min_max([1, 2, 3, 4, 5]))


class TestChangeMinMax(unittest.TestCase):
    def test_1(self):
        self.assertEqual([5, 2, 3, 4, 1], change_min_max([1, 2, 3, 4, 5]))
        self.assertEqual([1, 1, 1, 1], change_min_max([1, 1, 1, 1]))
        self.assertEqual([4, 23, -4, -2], change_min_max([4, -4, 23, -2]))