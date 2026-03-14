def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("НСД:", gcd(a, b))


















def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)


number = int(input("Введите число: "))
print("Сумма цифр:", sum_digits(number))













def is_symmetric(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_symmetric(lst[1:-1])


numbers = list(map(int, input("Введите числа через пробел: ").split()))

if is_symmetric(numbers):
    print("Список симметричный")
else:
    print("Список не симметричный")