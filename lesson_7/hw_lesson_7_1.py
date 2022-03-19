#1. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import unittest


def finding_median(arr: list):
    if (len(arr) % 2) != 1:
        return False

    def fast_sort_func(array: list):
        if len(array) < 2:
            return array
        else:
            mid_index = (len(array)) // 2
            left_part = [i for i in array if i < array[mid_index]]
            right_part = [i for i in array if i > array[mid_index]]
            return fast_sort_func(left_part) + [array[mid_index]] + fast_sort_func(right_part)

    result = fast_sort_func(arr)

    print(result)
    return result[(len(arr) // 2)]


print(finding_median([5, 4, 1, 3, 10, 6, 0]))


class TestFindingMedian(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, finding_median([5, 4, 1, 3, 10, 6, 0]))
        self.assertEqual(3, finding_median([1, 2, 3, 4, 5]))
        self.assertEqual(False, finding_median([1, 2, 3, 4, 5, 6]))
        self.assertEqual(1, finding_median([1]))