import string
import random


def generate_random_text(length):
    # Создаем список всех доступных символов
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Генерируем случайные символы и собираем их в строку
    random_text = ''.join(random.choices(all_chars, k=length))

    return random_text


# Запрашиваем у пользователя количество символов
num_chars = int(input("Введите количество символов: "))

# Генерируем и выводим случайный текст
random_output = generate_random_text(num_chars)
print(random_output)
