import itertools

def print_permutations():
    user_input = input("Введите строку: ")

    permutations = itertools.permutations(user_input)

    for perm in permutations:

        print(''.join(perm))

print_permutations()
