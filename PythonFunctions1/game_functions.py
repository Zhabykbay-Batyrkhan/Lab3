import random

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
            if code_index == len(code):
                return True
    return False

def sphere_volume(radius):
    import math
    return (4/3) * math.pi * (radius ** 3)

def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

def guess_the_number():
    print("Привет, как тебя зовут?")
    name = input()

    print(f"{name}, Выбери число от 1 до 20.")
    number_to_guess = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Попробуй угадать.")
        guess = int(input())
        guesses_taken += 1

        if guess < number_to_guess:
            print("Твое число слишком мало.")
        elif guess > number_to_guess:
            print("Твое число слишком много.")
        else:
            print(f"Отлично, {name}! Ты нашел мое число с {guesses_taken} попытки!")
            break

from game_functions import has_33, spy_game, sphere_volume

print(has_33([1, 3, 3]))  # True
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(sphere_volume(5))  # Выведет объем для радиуса 5


