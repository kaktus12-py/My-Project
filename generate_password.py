from random import choices
from string import ascii_letters, digits

def generate_password(m):
    SYMBOLS = ascii_letters + digits
    a = choices(SYMBOLS, k=m)
    return ''.join(a)


def main(n, m):
    password_set = set()
    while len(password_set) < n:
        password_set.add(generate_password(m))
    return list(password_set)

# print(*main(1, 1), sep="\n")
