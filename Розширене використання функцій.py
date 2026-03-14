def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


a = int(input("Введите число: "))
n = int(input("Введите степень: "))

print("Результат:", power(a, n))









def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False










import random

numbers = [random.randint(1, 100) for _ in range(100)]

def find_min_sum(lst, index=0, min_sum=None, min_index=0):

    if index > len(lst) - 10:
        return min_index

    current_sum = sum(lst[index:index+10])

    if min_sum is None or current_sum < min_sum:
        min_sum = current_sum
        min_index = index

    return find_min_sum(lst, index + 1, min_sum, min_index)


position = find_min_sum(numbers)

print("Список:", numbers)
print("Позиция минимальной суммы 10 чисел:", position)