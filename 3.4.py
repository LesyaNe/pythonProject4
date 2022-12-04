# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('Введите число:\n'))
fib_number = []

def get_fib(n):
    a, b = 1, 1
    for i in range(n):
        fib_number.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fib_number.insert(0, a)
        a, b = b, a - b
    return fib_number

print(get_fib(n))
