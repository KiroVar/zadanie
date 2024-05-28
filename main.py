import random
import string

from omnis_random import randfloat, ALPHABET
from datetime import datetime


def main() -> None:
    a = randfloat(1, 5, int(datetime.now().timestamp()))
    b = randfloat(1, 5, 1 + int(datetime.now().timestamp()))
    c = tuple(ALPHABET)
    print(a, b, c)


def generate_random_text(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    random_text = ''.join(random.choices(all_chars, k=length))
    return random_text


num_chars = int(input("Егорка, введи кол-во символов: "))
random_output = generate_random_text(num_chars)
print(random_output)

if __name__ == '__main__':
    pass
