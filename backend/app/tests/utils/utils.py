import random
import string


def random_ascii_string() -> str:
    return "".join(random.choices(string.ascii_letters, k=random.randint(5, 30)))
