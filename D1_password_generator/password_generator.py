import random

dictionary = open('dict.txt', 'r')
w_dict = [line for line in dictionary]


def generate_password():
    password = ''
    word_count = 0

    while word_count < 12:
        word = random.choice(w_dict)
        if word not in password:
            password = password+word
            word_count += 1
    password = password.replace('\n', ' ')
    return password


print(generate_password())
