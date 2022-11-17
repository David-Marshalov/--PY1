import string
import random
def get_random_password(long_=8) -> str:
    x = (string.ascii_uppercase + string.ascii_lowercase + string.digits)
    return random.sample(x, long_)
    # TODO написать функцию генерации случайных паролей

print(get_random_password(4))