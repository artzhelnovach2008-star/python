# Меню
def menu():
    print("\nМЕНЮ")
    print("1 - Крест (X)")
    print("2 - Треугольник вправо")
    print("3 - Треугольник влево")
    print("4 - Треугольник вверх")
    print("5 - Треугольник вниз")
    print("0 - Выход")


# 1. Крест (X)
def cross():
    size = 7
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# 2. Треугольник вправо
def triangle_right():
    for i in range(1, 6):
        print("*" * i)


# 3. Треугольник влево
def triangle_left():
    for i in range(1, 6):
        print(" " * (5 - i) + "*" * i)


# 4. Треугольник вверх
def triangle_up():
    for i in range(5, 0, -1):
        print(" " * (5 - i) + "*" * (i * 2 - 1))


# 5. Треугольник вниз
def triangle_down():
    for i in range(1, 6):
        print(" " * (5 - i) + "*" * (i * 2 - 1))


# Главная программа
while True:
    menu()
    choice = input("Выбери пункт меню: ")

    if choice == "1":
        cross()
    elif choice == "2":
        triangle_right()
    elif choice == "3":
        triangle_left()
    elif choice == "4":
        triangle_up()
    elif choice == "5":
        triangle_down()
    elif choice == "0":
        print("Выход из программы")
        break
    else:
        print("Неверный выбор!")
