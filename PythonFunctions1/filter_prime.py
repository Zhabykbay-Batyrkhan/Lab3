import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):

    return [num for num in numbers if is_prime(num)]

# Пример:
numbers = [10, 23, 4, 5, 50, 31, 2, 7, 19]
prime_numbers = filter_prime(numbers)
print(prime_numbers)
