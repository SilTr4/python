# 2) Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import unittest

def letters_numbers(letters: str):
    f_letter = ord(letters[0].lower()) - 96
    s_letter = ord(letters[1].lower()) - 96 # Порядковый номер в алфавите.
    if f_letter != s_letter:
        len_btw_letters = abs(f_letter - s_letter) - 1
    else:
        len_btw_letters = 0
    print(f_letter, s_letter)
    return len_btw_letters  # Кол-во букв между введенными.

print(letters_numbers('AZ'))

class TestLetNumb(unittest.TestCase):
    def test_1(self):
        self.assertEqual(24, letters_numbers('Az'))
        self.assertEqual(0, letters_numbers('ba'))
        self.assertEqual(0, letters_numbers('AA'))