import random

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

guess_the_number()
