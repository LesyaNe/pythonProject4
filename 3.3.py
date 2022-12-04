# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
#
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10
# d = ""
# n = int(input("Введите число:\n"))
# while n != 0:
#     d = str(n % 2) + d
#     n //= 2
# print(d)
#либо

n = int(input('Введите число:\n'))
def conver_to_bin(n):
    bin_n = ''
    while n > 0:
        bin_n += str(n % 2)
        n = n // 2
    return bin_n[::-1]

print(conver_to_bin(n))