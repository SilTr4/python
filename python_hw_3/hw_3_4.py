# 4. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import unittest


def finding_two_min_elem(arr: list):
    first_min = 0
    second_min = -1
    for i in range(1, len(arr)):
        if arr[first_min] >= arr[i]:
            second_min = first_min
            first_min = i
        elif arr[second_min] > arr[i]:
            second_min = i
    print(arr[first_min], arr[second_min])
    return arr[first_min], arr[second_min]


finding_two_min_elem([2, 3, 3])


class TestFindingTwoMinElem(unittest.TestCase):
    def test_1(self):
        self.assertEqual((1, 2), finding_two_min_elem([1, 2, 3, 4, 5]))
        self.assertEqual((1, 1), finding_two_min_elem([1, 1, 1, 1]))
        self.assertEqual((-4, -2), finding_two_min_elem([4, -4, 23, -2]))