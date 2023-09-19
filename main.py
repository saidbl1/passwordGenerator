import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)


def generate_password():
    len_password = int(input("How long would you like your password to be? "))
    # print(characters)

    random.shuffle(characters)
    # print(characters)

    password = []

    for i in range(len_password):
        password.append(random.choice(characters))

    password = "".join(password)

    print("Your password: \033[92m" + password + "\033[0m")


generate_password()
