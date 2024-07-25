import math
#Алгоритм для нахождения максимального/минимального числа
def find_max(list):
    # создаём переменную для хранения максимального числа в массиве
    max_number = list[0]

    for i in list:
        if i > max_number:
            max_number = i
    return max_number

numbers = [56, 74, 23, 98, 143, -89, -23]
print(find_max(numbers))
def find_min(list):
    # создаём переменную для хранения максимального числа в массиве
    min_number = list[0]

    for i in list:
        if i < min_number:
            min_number = i
    return min_number

numbers = [56, 74, 23, 98, 143, -89, -23]
print(find_min(numbers))

#Алгоритм для нахождения факториала
#5! = 1 * 2 * 3 * 4 * 5 = 120

def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial(5))

#Алгоритм для нахождения простого числа:
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(2))
print(is_prime(16))
print(is_prime(17591))