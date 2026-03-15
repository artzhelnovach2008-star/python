# Завдання 1
# Розрахунок фінальної ціни товару

try:
    price = float(input("Введіть початкову ціну товару: "))
    discount = float(input("Введіть відсоток знижки: "))

    final_price = price - (price * discount / 100)

    print("Фінальна ціна:", final_price)

except ValueError:
    print("Помилка: потрібно вводити тільки числа.")






# Завдання 2
# Переведення доларів у євро

try:
    dollars = float(input("Введіть суму в доларах: "))
    rate = float(input("Введіть курс обміну на євро: "))

    if rate == 0:
        raise Exception("Курс обміну не може дорівнювати нулю")

    euro = dollars * rate
    print("Сума в євро:", euro)

except ValueError:
    print("Помилка: введено некоректне число.")

except Exception as e:
    print("Помилка:", e)

finally:
    print("Операцію завершено.")









# Завдання 3
# Обчислення середнього значення оцінок

try:
    grades_input = input("Введіть оцінки через пробіл: ")

    grades_list = grades_input.split()

    numbers = []
    for grade in grades_list:
        numbers.append(float(grade))

    average = sum(numbers) / len(numbers)

    print("Середнє значення:", average)

except ValueError:
    print("Помилка: одне із значень не є числом.")

except ZeroDivisionError:
    print("Помилка: список оцінок порожній.")

finally:
    print("Завершення обчислень.")













# Завдання 4
# Симулятор банкомату

balance = 1000

try:
    amount = int(input("Введіть суму для зняття: "))

    if amount % 10 != 0 or amount > balance:
        raise Exception("Некоректна сума для зняття")

    print("Гроші успішно знято:", amount)

except ValueError:
    print("Помилка: введіть правильне число.")

except Exception as e:
    print("Помилка:", e)

finally:
    print("Транзакцію завершено.")














# Завдання 5
# Перевірка номера замовлення

try:
    order_number = input("Введіть номер замовлення: ")

    if order_number.startswith("ORD") and order_number[3:].isdigit():
        print("Номер замовлення правильний.")
    else:
        raise Exception("Неправильний формат номера замовлення")

except Exception as e:
    print("Помилка:", e)

finally:
    print("Перевірку завершено.")















# Завдання 6
# Обробка послідовності чисел

try:
    text = input("Введіть числа через пробіл: ")
    items = text.split()

    numbers = []

    for item in items:
        try:
            num = float(item)
            numbers.append(num)
        except ValueError:
            print("Попередження: значення", item, "пропущено, бо воно некоректне.")

    total = sum(numbers)
    average = total / len(numbers)

    print("Сума:", total)
    print("Середнє значення:", average)

except ZeroDivisionError:
    print("Помилка: немає правильних чисел для обчислення.")

finally:
    print("Обробку даних завершено.")