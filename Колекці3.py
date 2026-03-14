nums = list(map(int, input("Введіть числа через пробіл: ").split()))

unique = set(nums)

print("Унікальні елементи:", unique)







import random

set1 = {random.randint(1, 20) for _ in range(10)}
set2 = {random.randint(1, 20) for _ in range(10)}

print("Множина 1:", set1)
print("Множина 2:", set2)

print("Спільні елементи:", set1 & set2)
print("Різниця:", set1 - set2)
print("Об'єднання:", set1 | set2)











word1 = input("Введіть перше слово: ").lower()
word2 = input("Введіть друге слово: ").lower()

if set(word1) == set(word2):
    print("Це анаграми")
else:
    print("Це не анаграми")












