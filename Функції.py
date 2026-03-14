def show_text():
    print('"Don\'t compare yourself with anyone in this world..."')
    print("    if you do so, you are insulting yourself.")
    print("        Bill Gates")

show_text()











def show_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

show_even(a, b)








def draw_square(size, symbol, filled):
    
    for i in range(size):
        for j in range(size):

            if filled:
                print(symbol, end=" ")
            else:
                if i == 0 or i == size-1 or j == 0 or j == size-1:
                    print(symbol, end=" ")
                else:
                    print(" ", end=" ")

        print()


draw_square(5, "*", True)   # заполненный
print()
draw_square(5, "*", False)  # пустой










def count_digits(n):
    n = abs(n)
    return len(str(n))


num = int(input("Введите число: "))
print("Количество цифр:", count_digits(num))







def is_palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False


num = int(input("Введите число: "))

if is_palindrome(num):
    print("Это палиндром")
else:
    print("Это не палиндром")