a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

suma = a + b + c
dobutok = a * b * c

print("Сума:", suma)
print("Добуток:", dobutok)








d1 = float(input("Введіть першу діагональ: "))
d2 = float(input("Введіть другу діагональ: "))

area = (d1 * d2) / 2

print("Площа ромба:", area)









salary = float(input("Введіть зарплату за місяць: "))
credit = float(input("Введіть щомісячний платіж за кредитом: "))
utilities = float(input("Введіть платіж за комунальні послуги: "))

left = salary - credit - utilities

print("Залишиться грошей:", left)








distance = float(input("Введіть відстань (км): "))
fuel_per_100 = float(input("Введіть витрату палива на 100 км (л): "))
price_per_liter = float(input("Введіть ціну за 1 літр бензину: "))

liters = distance * fuel_per_100 / 100
cost = liters * price_per_liter

print("Витрачено палива (л):", liters)
print("Вартість поїздки:", cost)



