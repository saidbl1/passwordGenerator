import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()?/")


def generate_password():
    len_password = int(input("How long would you like your password to be? "))
    # print(characters)

    random.shuffle(characters)
    # print(characters)

    password = []

    for i in range(len_password):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


generate_password()
