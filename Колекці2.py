contacts = {}

while True:
    print("\nМеню:")
    print("1 - Додати контакт")
    print("2 - Видалити контакт")
    print("3 - Змінити контакт")
    print("4 - Показати всі контакти")
    print("5 - Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        name = input("Ім'я: ")
        phone = input("Телефон: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Ім'я для видалення: ")
        contacts.pop(name, None)

    elif choice == "3":
        name = input("Ім'я: ")
        if name in contacts:
            contacts[name] = input("Новий телефон: ")
        else:
            print("Контакт не знайдено")

    elif choice == "4":
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "5":
        break









text = input("Введіть текст: ").lower()

words = text.split()

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word, num in count.items():
    print(word, ":", num)











rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("Введіть валюту (USD/EUR/PLN): ").upper()
uah = float(input("Введіть суму в гривнях: "))

if currency in rates:
    result = uah / rates[currency]
    print("Отримаєте:", result, currency)
else:
    print("Валюта не знайдена")









dictionary = {
    "hello": "привіт",
    "book": "книга",
    "dog": "собака",
    "cat": "кіт",
    "sun": "сонце"
}

word = input("Введіть слово англійською: ").lower()

if word in dictionary:
    print("Переклад:", dictionary[word])
else:
    print("Слово не знайдено")