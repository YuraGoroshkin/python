import random
import string


# def random_phone_number():
#     number = str(random.randrange(9000000000, 9999999999))
#     return '8' + number
#
# print(random_phone_number())

# def random_year():
#     number = str(random.randint(1000, 3000))
#     return number
#
# print(random_year())


def random_email():
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

print(random_email())