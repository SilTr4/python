# 5) Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

import unittest

def list_sorting(arr: list):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    while j < len(arr):  # Допускается ли тут While или лучше прописать еще 1 цикл: for i in range(j, len(arr)): ?
        arr[j] = 0                                                                    # if arr[i] != 0:
        j += 1                                                                        # arr[j] = 0; j += 1
    return arr

print(list_sorting([1, 3, 6, 0, 6, 7, 0, 0, 0, 1]))

class TestIsListSorting(unittest.TestCase):
    def test_1(self):
        self.assertEqual([1, 3, 6, 6, 7, 1, 0, 0, 0, 0], list_sorting([1, 3, 6, 0, 6, 7, 0, 0, 0, 1]))
        self.assertEqual([0, 0, 0, 0, 0], list_sorting([0, 0, 0, 0, 0]))
        self.assertEqual([3, 2, 1, 5, 6], list_sorting([3, 2, 1, 5, 6]))