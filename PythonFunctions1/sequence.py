def spy_game(nums):
    code = [0, 0, 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
            if code_index == len(code):
                return True
    return False

# Примеры:
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
