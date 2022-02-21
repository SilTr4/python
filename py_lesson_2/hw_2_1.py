# 1) Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import unittest


def cnt_of_nmb(numb: int):
    even_numb = 0
    odd_numb = 0
    if numb == 0:
        even_numb = 1
    while numb != 0:
        numb_checker = numb % 10
        if numb_checker % 2 != 0:
            odd_numb += 1
        else:
            even_numb += 1
        numb = numb // 10
    print(f'Четных чисел: {even_numb}, нечетных чисел: {odd_numb}.')
    return even_numb, odd_numb


cnt_of_nmb(12348)


class TestCntOfNmb(unittest.TestCase):
    def test_1(self):
        self.assertEqual((3, 2), cnt_of_nmb(12308))
        self.assertEqual((1, 0), cnt_of_nmb(0))
        self.assertEqual((0, 4), cnt_of_nmb(9999))
