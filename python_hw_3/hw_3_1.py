# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def cnt_numbs():
    result = int
    for i in range(2, 10):
        result = 99 // i
        print(f'{i} = {result}')


cnt_numbs()

"""
2 = 49
3 = 33
4 = 24
5 = 19
6 = 16
7 = 14
8 = 12
9 = 11 """