# 4) Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
# such that each unique element appears only once. The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums. More formally,
# if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

import unittest

def make_non_dub_lst(arr: list):
    const = arr[0]
    j = 1
    for i in range(1, len(arr)):
        if const != arr[i]:
            arr[j] = arr[i]
            const = arr[i]
            j += 1
    result = j
    while j < len(arr):
        arr[j] = '_'
        j += 1
    return result, arr

print(make_non_dub_lst([1, 2, 2, 2, 4, 4, 4, 6]))

class TestMakeNonDubLst(unittest.TestCase):
    def test_1(self):
        self.assertEqual((4, [1, 2, 4, 6, '_', '_', '_', '_']), make_non_dub_lst([1, 2, 2, 2, 4, 4, 4, 6]))
        self.assertEqual((1, [0, '_', '_', '_', '_', '_', '_', '_']), make_non_dub_lst([0, 0, 0, 0, 0, 0, 0, 0]))
        self.assertEqual((8, [1, 2, 3, 4, 5, 6, 7, 8]), make_non_dub_lst([1, 2, 3, 4, 5, 6, 7, 8]))