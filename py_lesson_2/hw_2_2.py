# 2) Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843. (Сделать без использования строк)

import unittest


def numb_revers(numb: int):
    rev_num = 0
    const = 10
    while numb != 0:
        rev_num = rev_num * const + numb % 10
        numb //= 10
    return rev_num


print(numb_revers(123456789))


class TestNumbRevers(unittest.TestCase):
    def test_1(self):
        self.assertEqual(987654321, numb_revers(123456789))
        self.assertEqual(0, numb_revers(0))
        self.assertEqual(999, numb_revers(999))
