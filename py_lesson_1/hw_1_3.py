# 3) Определить, является ли год, который ввел пользователем, високосным или не високосным.

import unittest

def is_year_leap(year: int) -> bool:
    result = True
    if year % 4:
        result = False
    return result

print(is_year_leap(10))

class TestIsYearLeap(unittest.TestCase):
    def test_1(self):
        self.assertEqual(False, is_year_leap(1001))
        self.assertEqual(True, is_year_leap(0))