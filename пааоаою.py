start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

print("Числа, кратні 7:")

for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)







start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

# 1. Всі числа діапазону
print("Всі числа діапазону:")
for number in range(start, end + 1):
    print(number)

# 2. Всі числа в спадному порядку
print("Числа в спадному порядку:")
for number in range(end, start - 1, -1):
    print(number)

# 3. Числа, кратні 7
print("Числа, кратні 7:")
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number)

# 4. Кількість чисел, кратних 5
count = 0
for number in range(start, end + 1):
    if number % 5 == 0:
        count += 1

print("Кількість чисел, кратних 5:", count)















start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

























start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
step = int(input("Введіть крок: "))

order = input("Введіть порядок (прямий / зворотний): ")

if order == "прямий":
    for number in range(start, end + 1, step):
        print(number)
elif order == "зворотний":
    for number in range(end, start - 1, -step):
        print(number)
else:
    print("Невірний вибір порядку")














start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

# Нормалізація діапазону
if start > end:
    start, end = end, start

product = 1
found = False

for number in range(start, end + 1):
    if number % 4 == 0 and number % 6 != 0:
        product *= number
        found = True

if found:
    print("Добуток чисел:", product)
else:
    print("Чисел, що діляться на 4 але не діляться на 6, немає.")














A = int(input("Введіть число A: "))
N = int(input("Введіть степінь N: "))

result = 1

for i in range(N):
    result = result * A

print("Результат:", result)
