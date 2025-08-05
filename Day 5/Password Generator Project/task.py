import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

def first_version():
    password = ""

    for _ in range(nr_letters):
        rand_letter = random.randint(0, len(letters) - 1)
        password += letters[rand_letter]

    for _ in range(nr_symbols):
        rand_symbol = random.randint(0, len(symbols) - 1)
        password += symbols[rand_symbol]

    for _ in range(nr_numbers):
        rand_number = random.randint(0, len(numbers) - 1)
        password += numbers[rand_number]

    print(password)

first_version()